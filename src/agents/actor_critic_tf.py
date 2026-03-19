"""
Refactored Actor-Critic Networks with Architecture Factory Pattern

This module implements a TCN-focused architecture system supporting:
- TCN (Temporal Convolutional Network) for sequence processing
- TCN+Attention for advanced temporal feature extraction
- TCN+Fusion for hierarchical asset/context fusion

All architectures output Dirichlet distribution parameters for portfolio weights.
"""

import tensorflow as tf
from tensorflow.keras import layers, Model # type: ignore
import numpy as np
from typing import List, Tuple, Optional, Dict, Any
from src import config
from src.config import PHASE1_CONFIG

# Extract default values from config to use as fallbacks
_DEFAULT_AGENT_PARAMS = PHASE1_CONFIG.get('agent_params', {})
_DEFAULT_TCN_FILTERS = _DEFAULT_AGENT_PARAMS.get('tcn_filters', [64, 128, 256])
_DEFAULT_TCN_DILATIONS = _DEFAULT_AGENT_PARAMS.get('tcn_dilations', [1, 2, 4, 8, 16])
_DEFAULT_TCN_KERNEL_SIZE = _DEFAULT_AGENT_PARAMS.get('tcn_kernel_size', 3)
_DEFAULT_TCN_DROPOUT = _DEFAULT_AGENT_PARAMS.get('tcn_dropout', 0.2)
_DEFAULT_ACTOR_HIDDEN_DIMS = _DEFAULT_AGENT_PARAMS.get('actor_hidden_dims', [768, 512, 256, 128])
_DEFAULT_CRITIC_HIDDEN_DIMS = _DEFAULT_AGENT_PARAMS.get('critic_hidden_dims', [768, 512, 256, 128])
_DEFAULT_ATTENTION_HEADS = _DEFAULT_AGENT_PARAMS.get('attention_heads', 4)
_DEFAULT_ATTENTION_DIM = _DEFAULT_AGENT_PARAMS.get('attention_dim', 64)
_DEFAULT_ATTENTION_DROPOUT = _DEFAULT_AGENT_PARAMS.get('attention_dropout', 0.1)
_DEFAULT_FUSION_EMBED_DIM = _DEFAULT_AGENT_PARAMS.get('fusion_embed_dim', 128)
_DEFAULT_FUSION_HEADS = _DEFAULT_AGENT_PARAMS.get('fusion_attention_heads', 4)
_DEFAULT_FUSION_DROPOUT = _DEFAULT_AGENT_PARAMS.get('fusion_dropout', 0.1)
_DEFAULT_FUSION_ALPHA_HEAD_HIDDEN_DIMS = _DEFAULT_AGENT_PARAMS.get('fusion_alpha_head_hidden_dims', [])
_DEFAULT_FUSION_ALPHA_HEAD_DROPOUT = _DEFAULT_AGENT_PARAMS.get('fusion_alpha_head_dropout', _DEFAULT_FUSION_DROPOUT)
_DEFAULT_FUSION_CROSS_ASSET_MIXER_ENABLED = bool(_DEFAULT_AGENT_PARAMS.get('fusion_cross_asset_mixer_enabled', False))
_DEFAULT_FUSION_CROSS_ASSET_MIXER_LAYERS = int(_DEFAULT_AGENT_PARAMS.get('fusion_cross_asset_mixer_layers', 1))
_DEFAULT_FUSION_CROSS_ASSET_MIXER_EXPANSION = float(_DEFAULT_AGENT_PARAMS.get('fusion_cross_asset_mixer_expansion', 2.0))
_DEFAULT_FUSION_CROSS_ASSET_MIXER_DROPOUT = _DEFAULT_AGENT_PARAMS.get('fusion_cross_asset_mixer_dropout', _DEFAULT_FUSION_DROPOUT)
_DEFAULT_FUSION_ASSET_IDENTITY_ENABLED = bool(_DEFAULT_AGENT_PARAMS.get('fusion_asset_identity_enabled', False))
_DEFAULT_FUSION_CONTEXT_CROSS_ATTN_ENABLED = bool(_DEFAULT_AGENT_PARAMS.get('fusion_context_cross_attention_enabled', False))
_DEFAULT_FUSION_CONTEXT_CROSS_ATTN_HEADS = int(_DEFAULT_AGENT_PARAMS.get('fusion_context_cross_attention_heads', 4))
_DEFAULT_FUSION_CONTEXT_CROSS_ATTN_DROPOUT = float(_DEFAULT_AGENT_PARAMS.get('fusion_context_cross_attention_dropout', 0.1))
_DEFAULT_FUSION_PER_ASSET_ALPHA_HEAD = bool(_DEFAULT_AGENT_PARAMS.get('fusion_per_asset_alpha_head', False))
_DEFAULT_RECURRENT_MEMORY_ENABLED = bool(_DEFAULT_AGENT_PARAMS.get('recurrent_memory_enabled', False))
_DEFAULT_RECURRENT_MEMORY_UNITS = int(_DEFAULT_AGENT_PARAMS.get('recurrent_memory_units', 64))
_DEFAULT_RECURRENT_MEMORY_DROPOUT = float(_DEFAULT_AGENT_PARAMS.get('recurrent_memory_dropout', _DEFAULT_TCN_DROPOUT))
_DEFAULT_REGIME_CONDITIONING_ENABLED = bool(_DEFAULT_AGENT_PARAMS.get('regime_conditioning_enabled', False))
_DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM = int(_DEFAULT_AGENT_PARAMS.get('regime_conditioning_hidden_dim', 32))
_DEFAULT_REGIME_CONDITIONING_DROPOUT = float(_DEFAULT_AGENT_PARAMS.get('regime_conditioning_dropout', 0.0))
_DEFAULT_REGIME_CONDITIONING_MODE = str(_DEFAULT_AGENT_PARAMS.get('regime_conditioning_mode', 'concat'))
_DEFAULT_STATE_AUGMENTATION_ENABLED = bool(_DEFAULT_AGENT_PARAMS.get('state_augmentation_enabled', False))
_DEFAULT_DISTRIBUTIONAL_CRITIC_ENABLED = bool(_DEFAULT_AGENT_PARAMS.get('distributional_critic_enabled', False))
_DEFAULT_DISTRIBUTIONAL_NUM_QUANTILES = int(_DEFAULT_AGENT_PARAMS.get('distributional_num_quantiles', 17))
_DEFAULT_ALPHA_ACTIVATION = _DEFAULT_AGENT_PARAMS.get('dirichlet_alpha_activation', 'elu')
_DEFAULT_EXP_CLIP = tuple(_DEFAULT_AGENT_PARAMS.get('dirichlet_exp_clip', (-5.0, 3.0)))
_DEFAULT_DUAL_HEAD_ENABLED = bool(_DEFAULT_AGENT_PARAMS.get('dual_head_enabled', False))
_DEFAULT_MIXTURE_DIRICHLET_ENABLED = bool(_DEFAULT_AGENT_PARAMS.get('mixture_dirichlet_enabled', False))
_DEFAULT_MIXTURE_DIRICHLET_COMPONENTS = int(_DEFAULT_AGENT_PARAMS.get('mixture_dirichlet_num_components', 3))
_DEFAULT_MIXTURE_DIRICHLET_GATING_HIDDEN_DIMS = list(
    _DEFAULT_AGENT_PARAMS.get('mixture_dirichlet_gating_hidden_dims', [64])
)
_DEFAULT_MIXTURE_DIRICHLET_COMPONENT_HIDDEN_DIMS = list(
    _DEFAULT_AGENT_PARAMS.get('mixture_dirichlet_component_hidden_dims', [64])
)
_RUNTIME_STATE_AUGMENTATION_ENABLED = _DEFAULT_STATE_AUGMENTATION_ENABLED


def _to_tensor_with_cast(value: Any, dtype: Optional[tf.dtypes.DType] = None) -> tf.Tensor:
    """Convert to tensor and cast dtype explicitly (safe with mixed precision tensors)."""
    tensor = tf.convert_to_tensor(value)
    if dtype is not None:
        target_dtype = tf.dtypes.as_dtype(dtype)
        if tensor.dtype != target_dtype:
            tensor = tf.cast(tensor, target_dtype)
    return tensor


# ============================================================================
# ATTENTION MECHANISM
# ============================================================================

class MultiHeadSelfAttention(layers.Layer):
    """
    Multi-head self-attention mechanism for sequential data.
    
    Can be applied after TCN layers to learn important temporal relationships.
    """
    
    def __init__(self, d_model: int, num_heads: int, dropout: float = 0.1, name: str = "attention"):
        """
        Args:
            d_model: Dimension of the model (must be divisible by num_heads)
            num_heads: Number of attention heads
            dropout: Dropout rate
        """
        super(MultiHeadSelfAttention, self).__init__(name=name)
        
        assert d_model % num_heads == 0, f"d_model ({d_model}) must be divisible by num_heads ({num_heads})"
        
        self.d_model = d_model
        self.num_heads = num_heads
        self.depth = d_model // num_heads
        
        self.wq = layers.Dense(d_model, name=f'{name}_wq')
        self.wk = layers.Dense(d_model, name=f'{name}_wk')
        self.wv = layers.Dense(d_model, name=f'{name}_wv')
        
        self.dense = layers.Dense(d_model, name=f'{name}_output')
        self.dropout = layers.Dropout(dropout)
        self.layernorm = layers.LayerNormalization(epsilon=1e-6)
    
    def split_heads(self, x, batch_size):
        """Split the last dimension into (num_heads, depth)."""
        x = tf.reshape(x, (batch_size, -1, self.num_heads, self.depth))
        return tf.transpose(x, perm=[0, 2, 1, 3])
    
    def call(self, x, training=None):
        """
        Args:
            x: Input tensor of shape (batch, seq_len, d_model)
            
        Returns:
            Output tensor of shape (batch, seq_len, d_model)
        """
        batch_size = tf.shape(x)[0]
        
        # Linear projections
        q = self.wq(x)  # (batch, seq_len, d_model)
        k = self.wk(x)
        v = self.wv(x)
        
        # Split into multiple heads
        q = self.split_heads(q, batch_size)  # (batch, num_heads, seq_len, depth)
        k = self.split_heads(k, batch_size)
        v = self.split_heads(v, batch_size)
        
        # Scaled dot-product attention
        matmul_qk = tf.matmul(q, k, transpose_b=True)  # (batch, num_heads, seq_len, seq_len)
        
        # Scale
        # Keep scale dtype aligned with attention logits for mixed precision safety.
        dk = tf.cast(tf.shape(k)[-1], matmul_qk.dtype)
        scaled_attention_logits = matmul_qk / tf.math.sqrt(dk)
        
        # Softmax
        attention_weights = tf.nn.softmax(scaled_attention_logits, axis=-1)
        attention_weights = self.dropout(attention_weights, training=training)
        
        # Apply attention to values
        attention_output = tf.matmul(attention_weights, v)  # (batch, num_heads, seq_len, depth)
        
        # Concatenate heads
        attention_output = tf.transpose(attention_output, perm=[0, 2, 1, 3])
        concat_attention = tf.reshape(attention_output, (batch_size, -1, self.d_model))
        
        # Final linear projection
        output = self.dense(concat_attention)
        output = self.dropout(output, training=training)
        
        # Residual connection and layer norm
        output = self.layernorm(x + output)
        
        return output


class CrossAssetMixerBlock(layers.Layer):
    """
    Lightweight cross-asset mixer block:
    pre-norm self-attention + feed-forward residual.
    """

    def __init__(
        self,
        d_model: int,
        num_heads: int,
        expansion: float = 2.0,
        dropout: float = 0.1,
        name: str = "cross_asset_mixer",
    ):
        super(CrossAssetMixerBlock, self).__init__(name=name)
        if d_model % num_heads != 0:
            num_heads = 1
        hidden_dim = max(d_model, int(round(d_model * float(expansion))))

        self.norm_attn = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_norm_attn")
        self.attn = layers.MultiHeadAttention(
            num_heads=int(num_heads),
            key_dim=max(1, d_model // int(num_heads)),
            dropout=dropout,
            name=f"{name}_attn",
        )
        self.attn_dropout = layers.Dropout(dropout, name=f"{name}_attn_dropout")

        self.norm_ffn = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_norm_ffn")
        self.ffn_dense1 = layers.Dense(hidden_dim, activation="gelu", name=f"{name}_ffn_dense1")
        self.ffn_dropout1 = layers.Dropout(dropout, name=f"{name}_ffn_dropout1")
        self.ffn_dense2 = layers.Dense(d_model, activation=None, name=f"{name}_ffn_dense2")
        self.ffn_dropout2 = layers.Dropout(dropout, name=f"{name}_ffn_dropout2")

    def call(self, x, training=None):
        attn_in = self.norm_attn(x)
        attn_out = self.attn(attn_in, attn_in, training=training)
        attn_out = self.attn_dropout(attn_out, training=training)
        x = x + attn_out

        ffn_in = self.norm_ffn(x)
        ffn_out = self.ffn_dense1(ffn_in)
        ffn_out = self.ffn_dropout1(ffn_out, training=training)
        ffn_out = self.ffn_dense2(ffn_out)
        ffn_out = self.ffn_dropout2(ffn_out, training=training)
        return x + ffn_out


class ContextCrossAttentionBlock(layers.Layer):
    """
    Cross-attention block: per-asset queries attend to global context.

    Enables each asset embedding to selectively incorporate macro/market
    information (interest rates, VIX, breadth, etc.), producing
    context-aware per-asset representations.

    Q = per-asset embeddings  (batch, num_assets, d_model)
    K/V = global context      (batch, K, d_model)

    Architecture follows the pre-norm transformer convention with
    separate normalization on Q and K/V paths for stable cross-modal fusion.
    """

    def __init__(
        self,
        d_model: int,
        num_heads: int,
        expansion: float = 2.0,
        dropout: float = 0.1,
        name: str = "ctx_cross_attn",
    ):
        super(ContextCrossAttentionBlock, self).__init__(name=name)
        if d_model % num_heads != 0:
            num_heads = 1

        # Pre-norm for query and key/value paths
        self.norm_q = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_norm_q")
        self.norm_kv = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_norm_kv")

        # Multi-head cross-attention
        self.cross_attn = layers.MultiHeadAttention(
            num_heads=int(num_heads),
            key_dim=max(1, d_model // int(num_heads)),
            dropout=dropout,
            name=f"{name}_mha",
        )
        self.attn_dropout = layers.Dropout(dropout, name=f"{name}_attn_drop")

        # Feed-forward network (expansion -> projection)
        hidden_dim = max(d_model, int(round(d_model * float(expansion))))
        self.norm_ffn = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_norm_ffn")
        self.ffn_dense1 = layers.Dense(hidden_dim, activation="gelu", name=f"{name}_ffn1")
        self.ffn_drop1 = layers.Dropout(dropout, name=f"{name}_ffn_drop1")
        self.ffn_dense2 = layers.Dense(d_model, activation=None, name=f"{name}_ffn2")
        self.ffn_drop2 = layers.Dropout(dropout, name=f"{name}_ffn_drop2")

    def call(self, query, context, training=None):
        """
        Args:
            query:   (batch, num_assets, d_model) - per-asset embeddings
            context: (batch, K, d_model) - global context token(s)
        Returns:
            (batch, num_assets, d_model) - context-enriched asset embeddings
        """
        # Cross-attention: each asset attends to global context
        q = self.norm_q(query)
        kv = self.norm_kv(context)
        attn_out = self.cross_attn(q, kv, training=training)
        attn_out = self.attn_dropout(attn_out, training=training)
        x = query + attn_out  # residual

        # Feed-forward with residual
        ffn_in = self.norm_ffn(x)
        ffn_out = self.ffn_dense1(ffn_in)
        ffn_out = self.ffn_drop1(ffn_out, training=training)
        ffn_out = self.ffn_dense2(ffn_out)
        ffn_out = self.ffn_drop2(ffn_out, training=training)
        return x + ffn_out


# ============================================================================
# TCN (TEMPORAL CONVOLUTIONAL NETWORK) BLOCK
# ============================================================================

class TCNBlock(layers.Layer):
    """
    Temporal Convolutional Network block with dilated causal convolutions.
    
    TCNs are efficient alternatives to RNNs for sequence modeling, offering:
    - Parallel processing (unlike sequential RNNs)
    - Large receptive fields through dilations
    - Stable gradients
    """
    
    def __init__(self, 
                 filters: int, 
                 kernel_size: int = None, 
                 dilation_rate: int = 1,
                 dropout: float = None,
                 name: str = "tcn_block"):
        """
        Args:
            filters: Number of convolutional filters
            kernel_size: Size of the convolutional kernel
            dilation_rate: Dilation rate for the convolution
            dropout: Dropout rate
        """
        super(TCNBlock, self).__init__(name=name)
        
        # Apply config defaults
        if kernel_size is None:
            kernel_size = _DEFAULT_TCN_KERNEL_SIZE
        if dropout is None:
            dropout = _DEFAULT_TCN_DROPOUT
        
        self.conv1 = layers.Conv1D(
            filters=filters,
            kernel_size=kernel_size,
            dilation_rate=dilation_rate,
            padding='causal',
            activation='relu',
            name=f'{name}_conv1'
        )
        self.dropout1 = layers.Dropout(dropout)
        
        self.conv2 = layers.Conv1D(
            filters=filters,
            kernel_size=kernel_size,
            dilation_rate=dilation_rate,
            padding='causal',
            activation='relu',
            name=f'{name}_conv2'
        )
        self.dropout2 = layers.Dropout(dropout)
        
        self.downsample = None
        self.relu = layers.Activation('relu')
    
    def build(self, input_shape):
        """Build the layer (create downsample if needed)."""
        if input_shape[-1] != self.conv2.filters:
            self.downsample = layers.Conv1D(
                filters=self.conv2.filters,
                kernel_size=1,
                padding='same',
                name=f'{self.name}_downsample'
            )
    
    def call(self, x, training=None):
        """
        Args:
            x: Input tensor of shape (batch, seq_len, features)
            
        Returns:
            Output tensor of shape (batch, seq_len, filters)
        """
        # Residual connection
        residual = x
        
        # First convolution
        out = self.conv1(x)
        out = self.dropout1(out, training=training)
        
        # Second convolution
        out = self.conv2(out)
        out = self.dropout2(out, training=training)
        
        # Downsample residual if needed
        if self.downsample is not None:
            residual = self.downsample(residual)
        
        # Add residual and apply activation
        out = self.relu(out + residual)
        
        return out


def _flatten_structured_sequence_input(state: Any) -> tf.Tensor:
    """
    Accept either flat sequence tensor or structured dict {"asset": ..., "context": ...}
    and return a flat sequence tensor (batch, timesteps, features).
    """
    if not isinstance(state, dict):
        return _to_tensor_with_cast(state, tf.float32)

    asset = state.get("asset")
    if asset is None:
        raise ValueError("Structured state must include key 'asset'.")

    asset = _to_tensor_with_cast(asset, tf.float32)
    if asset.shape.rank == 3:
        asset = tf.expand_dims(asset, axis=0)
    if asset.shape.rank != 4:
        raise ValueError(
            f"Structured asset input must have rank 3 or 4, got shape {asset.shape}"
        )

    batch = tf.shape(asset)[0]
    timesteps = tf.shape(asset)[1]
    asset_flat = tf.reshape(asset, (batch, timesteps, -1))

    context = state.get("context")
    if context is None:
        return asset_flat

    context = _to_tensor_with_cast(context, asset_flat.dtype)
    if context.shape.rank == 1:
        context = tf.expand_dims(tf.expand_dims(context, axis=0), axis=0)
    elif context.shape.rank == 2:
        context = tf.expand_dims(context, axis=1)
    elif context.shape.rank == 3:
        pass
    else:
        raise ValueError(
            f"Structured context input must have rank 1, 2, or 3, got shape {context.shape}"
        )

    pad_time = tf.maximum(0, timesteps - tf.shape(context)[1])
    context = tf.pad(context, [[0, 0], [0, pad_time], [0, 0]])
    context = context[:, :timesteps, :]

    return tf.concat([asset_flat, context], axis=-1)


def _compute_regime_summary_features(
    sequence: tf.Tensor,
    *,
    include_state_augmentation: Optional[bool] = None,
) -> tf.Tensor:
    """
    Compact regime descriptor from a sequence tensor of shape (batch, timesteps, features).
    Produces a fixed-width summary per sample (5D base, 9D with augmentation).
    """
    x = _to_tensor_with_cast(sequence, tf.float32)
    if x.shape.rank != 3:
        raise ValueError(f"Regime summary expects rank-3 sequence, got {x.shape}")

    mean_level = tf.reduce_mean(x, axis=[1, 2])
    std_level = tf.math.reduce_std(x, axis=[1, 2])
    first_step = tf.reduce_mean(x[:, 0, :], axis=-1)
    last_step = tf.reduce_mean(x[:, -1, :], axis=-1)
    trend_level = last_step - first_step
    diffs = x[:, 1:, :] - x[:, :-1, :]
    diff_count = tf.cast(tf.shape(diffs)[1] * tf.shape(diffs)[2], x.dtype)
    diff_scale = tf.reduce_sum(tf.abs(diffs), axis=[1, 2]) / tf.maximum(diff_count, 1.0)
    abs_level = tf.reduce_mean(tf.abs(x), axis=[1, 2])
    base_features = [mean_level, std_level, trend_level, diff_scale, abs_level]

    if include_state_augmentation is None:
        include_state_augmentation = bool(_RUNTIME_STATE_AUGMENTATION_ENABLED)
    if not include_state_augmentation:
        return tf.stack(base_features, axis=-1)

    # Augmentation proxies are derived from sequence-level dynamics, no env schema changes required.
    step_signal = tf.reduce_mean(x, axis=-1)  # (batch, timesteps)
    neg_signal = tf.minimum(step_signal, 0.0)
    downside_semidev = tf.sqrt(tf.reduce_mean(tf.square(neg_signal), axis=1) + 1e-8)

    cum_signal = tf.cumsum(step_signal, axis=1)
    running_peak = tf.scan(
        lambda prev, curr: tf.maximum(prev, curr),
        tf.transpose(cum_signal, perm=[1, 0]),
        initializer=cum_signal[:, 0],
    )
    running_peak = tf.transpose(running_peak, perm=[1, 0])
    drawdown = cum_signal - running_peak
    max_drawdown_proxy = tf.reduce_min(drawdown, axis=1)

    drawdown_deltas = drawdown[:, 1:] - drawdown[:, :-1]
    drawdown_velocity_proxy = tf.reduce_mean(drawdown_deltas, axis=1)

    steps = tf.shape(step_signal)[1]
    time_axis = tf.linspace(tf.cast(0.0, x.dtype), tf.cast(1.0, x.dtype), tf.maximum(steps, 1))
    maturity_centered = (2.0 * time_axis) - 1.0
    late_early_trend = tf.reduce_mean(step_signal * maturity_centered[tf.newaxis, :], axis=1)

    return tf.stack(
        base_features
        + [downside_semidev, max_drawdown_proxy, drawdown_velocity_proxy, late_early_trend],
        axis=-1,
    )


class LearnedRegimeEncoder(layers.Layer):
    """Encode a sequence into a compact regime embedding for conditioning."""

    def __init__(
        self,
        embedding_dim: int,
        hidden_dim: int = 64,
        dropout: float = 0.0,
        name: str = "regime_encoder",
    ):
        super(LearnedRegimeEncoder, self).__init__(name=name)
        self.embedding_dim = int(embedding_dim)
        self.hidden_dim = max(16, int(hidden_dim))
        self.dropout_rate = float(max(0.0, dropout))

        self.input_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_input_norm")
        self.input_proj = layers.Dense(self.hidden_dim, activation="gelu", name=f"{name}_input_proj")
        self.conv1 = layers.Conv1D(
            self.hidden_dim,
            kernel_size=3,
            dilation_rate=1,
            padding="causal",
            activation="gelu",
            name=f"{name}_conv1",
        )
        self.conv2 = layers.Conv1D(
            self.hidden_dim,
            kernel_size=3,
            dilation_rate=2,
            padding="causal",
            activation="gelu",
            name=f"{name}_conv2",
        )
        self.block_dropout = layers.Dropout(self.dropout_rate, name=f"{name}_block_drop")
        self.attn_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_attn_norm")
        num_heads = 2 if self.hidden_dim >= 32 else 1
        self.self_attn = layers.MultiHeadAttention(
            num_heads=num_heads,
            key_dim=max(8, self.hidden_dim // num_heads),
            dropout=self.dropout_rate,
            name=f"{name}_self_attn",
        )
        self.attn_dropout = layers.Dropout(self.dropout_rate, name=f"{name}_attn_drop")
        self.ffn_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_ffn_norm")
        self.ffn_dense1 = layers.Dense(self.hidden_dim * 2, activation="gelu", name=f"{name}_ffn1")
        self.ffn_dense2 = layers.Dense(self.hidden_dim, activation=None, name=f"{name}_ffn2")
        self.ffn_dropout = layers.Dropout(self.dropout_rate, name=f"{name}_ffn_drop")
        self.pool_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_pool_norm")
        self.pool_score = layers.Dense(1, activation=None, name=f"{name}_pool_score")
        self.output_proj = layers.Dense(self.embedding_dim, activation=None, name=f"{name}_output")

    def call(self, sequence, training=None):
        x = _to_tensor_with_cast(sequence, tf.float32)
        if x.shape.rank != 3:
            raise ValueError(f"LearnedRegimeEncoder expects rank-3 sequence, got {x.shape}")

        x = self.input_norm(x)
        x = self.input_proj(x)
        residual = x
        x = self.conv1(x)
        x = self.block_dropout(x, training=training)
        x = self.conv2(x)
        x = self.block_dropout(x, training=training)
        x = x + residual

        attn_in = self.attn_norm(x)
        attn_out = self.self_attn(attn_in, attn_in, training=training)
        attn_out = self.attn_dropout(attn_out, training=training)
        x = x + attn_out

        ffn_in = self.ffn_norm(x)
        ffn_out = self.ffn_dense1(ffn_in)
        ffn_out = self.ffn_dropout(ffn_out, training=training)
        ffn_out = self.ffn_dense2(ffn_out)
        ffn_out = self.ffn_dropout(ffn_out, training=training)
        x = x + ffn_out

        pool_in = self.pool_norm(x)
        attn_logits = self.pool_score(pool_in)
        attn_weights = tf.nn.softmax(attn_logits, axis=1)
        pooled_attn = tf.reduce_sum(attn_weights * x, axis=1)
        pooled_mean = tf.reduce_mean(x, axis=1)
        pooled_last = x[:, -1, :]
        pooled = tf.concat([pooled_attn, pooled_mean, pooled_last], axis=-1)
        return self.output_proj(pooled)


class FiLMLayer(layers.Layer):
    """Feature-wise Linear Modulation (FiLM) layer.

    Given a conditioning signal z, produces scale (γ) and shift (β) vectors
    that modulate input features:

        output = γ * features + β

    where γ = Dense(z), β = Dense(z).

    This is more expressive than concat-based conditioning because it allows
    the conditioning signal to selectively amplify, dampen, or shift individual
    feature channels via multiplicative interaction.

    Reference: Perez et al. "FiLM: Visual Reasoning with a General Conditioning
    Layer" (AAAI 2018).
    """

    def __init__(
        self,
        feature_dim: int,
        conditioning_dim: int,
        hidden_dim: int = 32,
        dropout: float = 0.0,
        gamma_limit: float = 0.15,
        beta_limit: float = 0.10,
        name: str = "film_layer",
    ):
        super(FiLMLayer, self).__init__(name=name)
        self.feature_dim = int(feature_dim)
        self.conditioning_dim = int(conditioning_dim)
        self.gamma_limit = float(max(0.0, gamma_limit))
        self.beta_limit = float(max(0.0, beta_limit))

        # Conditioning encoder: z => hidden representation
        self.cond_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_cond_norm")
        self.cond_encoder = tf.keras.Sequential(
            [
                layers.Dense(hidden_dim, activation="gelu", name=f"{name}_cond_h1"),
                layers.Dense(hidden_dim, activation="gelu", name=f"{name}_cond_h2"),
            ],
            name=f"{name}_cond_encoder",
        )

        self.gamma_head = layers.Dense(
            self.feature_dim,
            activation=None,
            kernel_initializer=tf.keras.initializers.Zeros(),
            bias_initializer=tf.keras.initializers.Zeros(),
            name=f"{name}_gamma",
        )

        self.beta_head = layers.Dense(
            self.feature_dim,
            activation=None,
            kernel_initializer=tf.keras.initializers.Zeros(),
            bias_initializer=tf.keras.initializers.Zeros(),
            name=f"{name}_beta",
        )

        self.film_dropout = layers.Dropout(float(max(0.0, dropout)))
        self._last_modulation_stats: Dict[str, float] = {}

    def call(self, features, conditioning, training=None):
        """Apply FiLM modulation.

        Args:
            features: (batch, dim) or (batch, num_assets, dim) — features to modulate.
            conditioning: (batch, cond_dim) — regime summary features.
            training: Whether in training mode.

        Returns:
            Modulated features with same shape as input.
        """
        conditioning = self.cond_norm(conditioning)
        h = self.cond_encoder(conditioning, training=training)
        gamma_delta = self.gamma_limit * tf.tanh(self.gamma_head(h))
        beta = self.beta_limit * tf.tanh(self.beta_head(h))
        gamma = 1.0 + gamma_delta

        # Expand dims if features is 3D (per-asset): (batch, 1, dim)
        if features.shape.rank == 3:
            gamma = tf.expand_dims(gamma, axis=1)
            beta = tf.expand_dims(beta, axis=1)

        delta = ((gamma - 1.0) * features) + beta
        delta = self.film_dropout(delta, training=training)
        if tf.executing_eagerly():
            try:
                gamma_delta_np = gamma_delta.numpy()
                beta_np = beta.numpy() if beta.shape.rank == 2 else tf.squeeze(beta, axis=1).numpy()
                self._last_modulation_stats = {
                    "gamma_mean": float(np.mean(1.0 + gamma_delta_np)),
                    "gamma_std": float(np.std(1.0 + gamma_delta_np)),
                    "gamma_delta_abs_mean": float(np.mean(np.abs(gamma_delta_np))),
                    "gamma_sat_frac": float(np.mean(np.abs(gamma_delta_np) >= (0.95 * self.gamma_limit)))
                    if self.gamma_limit > 0.0 else 0.0,
                    "beta_abs_mean": float(np.mean(np.abs(beta_np))),
                    "beta_std": float(np.std(beta_np)),
                    "beta_sat_frac": float(np.mean(np.abs(beta_np) >= (0.95 * self.beta_limit)))
                    if self.beta_limit > 0.0 else 0.0,
                }
            except Exception:
                self._last_modulation_stats = {}
        return features + delta

    def get_modulation_stats(self, conditioning) -> Dict[str, float]:
        conditioning = _to_tensor_with_cast(conditioning, tf.float32)
        conditioning = self.cond_norm(conditioning)
        h = self.cond_encoder(conditioning, training=False)
        gamma_delta = self.gamma_limit * tf.tanh(self.gamma_head(h))
        beta = self.beta_limit * tf.tanh(self.beta_head(h))
        gamma = 1.0 + gamma_delta

        gamma_np = gamma.numpy()
        gamma_delta_np = gamma_delta.numpy()
        beta_np = beta.numpy()
        return {
            "gamma_mean": float(np.mean(gamma_np)),
            "gamma_std": float(np.std(gamma_np)),
            "gamma_delta_abs_mean": float(np.mean(np.abs(gamma_delta_np))),
            "gamma_sat_frac": float(np.mean(np.abs(gamma_delta_np) >= (0.95 * self.gamma_limit)))
            if self.gamma_limit > 0.0 else 0.0,
            "beta_abs_mean": float(np.mean(np.abs(beta_np))),
            "beta_std": float(np.std(beta_np)),
            "beta_sat_frac": float(np.mean(np.abs(beta_np) >= (0.95 * self.beta_limit)))
            if self.beta_limit > 0.0 else 0.0,
        }

    def get_last_modulation_stats(self) -> Dict[str, float]:
        return dict(self._last_modulation_stats)


def _build_regime_conditioning_modules(
    *,
    name: str,
    feature_dim: int,
    hidden_dim: int,
    dropout: float,
    mode: str,
    sequence_film_feature_dim: Optional[int] = None,
    latent_gamma_limit: float = 0.15,
    latent_beta_limit: float = 0.10,
    sequence_gamma_limit: float = 0.08,
    sequence_beta_limit: float = 0.05,
):
    hidden_dim = max(8, int(hidden_dim))
    dropout = float(max(0.0, dropout))
    mode = str(mode).lower().strip()
    encoder_hidden_dim = max(hidden_dim, min(256, int(feature_dim)))
    regime_sequence_encoder = LearnedRegimeEncoder(
        embedding_dim=hidden_dim,
        hidden_dim=encoder_hidden_dim,
        dropout=dropout,
        name=f"{name}_regime_encoder",
    )
    regime_sequence_film = None
    regime_film = None
    regime_fusion = None
    regime_dropout = None
    if mode == "film":
        regime_film = FiLMLayer(
            feature_dim=int(feature_dim),
            conditioning_dim=hidden_dim,
            hidden_dim=hidden_dim,
            dropout=dropout,
            gamma_limit=float(max(0.0, latent_gamma_limit)),
            beta_limit=float(max(0.0, latent_beta_limit)),
            name=f"{name}_regime_film",
        )
        if sequence_film_feature_dim is not None and int(sequence_film_feature_dim) > 0:
            regime_sequence_film = FiLMLayer(
                feature_dim=int(sequence_film_feature_dim),
                conditioning_dim=hidden_dim,
                hidden_dim=max(8, hidden_dim // 2),
                dropout=0.0,
                gamma_limit=float(max(0.0, sequence_gamma_limit)),
                beta_limit=float(max(0.0, sequence_beta_limit)),
                name=f"{name}_regime_sequence_film",
            )
    else:
        regime_fusion = layers.Dense(
            int(feature_dim),
            activation="gelu",
            name=f"{name}_regime_fusion",
        )
        regime_dropout = layers.Dropout(dropout)

    return regime_sequence_encoder, regime_sequence_film, regime_film, regime_fusion, regime_dropout


def _apply_regime_conditioning(
    features: tf.Tensor,
    regime_embedding: tf.Tensor,
    *,
    regime_film_layer: Optional[FiLMLayer],
    regime_fusion: Optional[layers.Layer],
    regime_dropout: Optional[layers.Dropout],
    training=None,
) -> tf.Tensor:
    if regime_embedding is None:
        return features
    if regime_film_layer is not None:
        return regime_film_layer(features, regime_embedding, training=training)
    if regime_fusion is None:
        return features

    cond = regime_embedding
    if features.shape.rank == 3:
        cond = tf.expand_dims(cond, axis=1)
        cond = tf.tile(cond, [1, tf.shape(features)[1], 1])
    fused = regime_fusion(tf.concat([features, cond], axis=-1), training=training)
    if regime_dropout is not None:
        fused = regime_dropout(fused, training=training)
    return fused


def _prefix_modulation_stats(prefix: str, stats: Dict[str, float]) -> Dict[str, float]:
    if not stats:
        return {}
    return {f"{prefix}_{key}": float(value) for key, value in stats.items()}


def _merge_modulation_stats(*stats_dicts: Dict[str, float]) -> Dict[str, float]:
    valid_stats = [stats for stats in stats_dicts if stats]
    if not valid_stats:
        return {}

    merged: Dict[str, float] = {}
    all_keys = set().union(*(stats.keys() for stats in valid_stats))
    for key in all_keys:
        values = [float(stats[key]) for stats in valid_stats if key in stats]
        if values:
            merged[key] = float(np.mean(values))
    return merged


# ============================================================================
# ACTOR NETWORKS
# ============================================================================

class DirichletActor(Model):
    """
    Base class that manages the adaptive Dirichlet epsilon schedule.
    """

    def __init__(
        self,
        *,
        name: str,
        epsilon_start: float = 0.5,
        epsilon_min: float = 0.1,
        alpha_activation: str = None,
        exp_clip: Tuple[float, float] = None,
        logit_temperature: float = 1.0,  # New parameter
        alpha_cap: float = None,         # New parameter
        adaptive_temperature_enabled: bool = False,
        adaptive_temperature_base: float = 1.0,
        adaptive_temperature_slope: float = 0.0,
        adaptive_temperature_min: float = 0.8,
        adaptive_temperature_max: float = 2.5,
        dual_head_enabled: bool = False,
        **kwargs,
    ):
        # Extract custom params before passing kwargs to Keras Layer
        self._exp_tanh_scale = float(kwargs.pop('exp_tanh_scale', 2.5))
        self._softplus_alpha_floor = float(kwargs.pop('softplus_alpha_floor', 0.0))
        self._softplus_alpha_scale = float(max(kwargs.pop('softplus_alpha_scale', 1.0), 1e-6))
        self._cross_sectional_standardize = bool(kwargs.pop('cross_sectional_standardize', False))
        super(DirichletActor, self).__init__(name=name, **kwargs)
        self._epsilon_max_value = float(epsilon_start)
        self._epsilon_min_value = float(epsilon_min)
        # Apply config defaults if not explicitly provided
        if alpha_activation is None:
            alpha_activation = _DEFAULT_ALPHA_ACTIVATION
        if exp_clip is None:
            exp_clip = _DEFAULT_EXP_CLIP
        self._alpha_activation = alpha_activation.lower().strip()
        self._exp_clip = exp_clip
        self._version_flag = "v2_updated"
        
        # Dirichlet Controls
        self._logit_temperature = float(logit_temperature) if logit_temperature else 1.0
        self._alpha_cap = float(alpha_cap) if alpha_cap else None
        self._adaptive_temperature_enabled = bool(adaptive_temperature_enabled)
        self._adaptive_temperature_base = float(max(adaptive_temperature_base, 1e-6))
        self._adaptive_temperature_slope = float(max(adaptive_temperature_slope, 0.0))
        temp_min = float(max(adaptive_temperature_min, 1e-6))
        temp_max = float(max(adaptive_temperature_max, temp_min))
        self._adaptive_temperature_min = temp_min
        self._adaptive_temperature_max = temp_max
        self._dual_head_enabled = bool(dual_head_enabled)

        self._dirichlet_epsilon = tf.Variable(
            float(epsilon_start),
            trainable=False,
            dtype=tf.float32,
            name=f"{name}_epsilon",
        )

    def epsilon_value(self) -> tf.Tensor:
        """Return the current epsilon tensor (clamped to >0)."""
        return tf.maximum(self._dirichlet_epsilon, 1e-6)

    def update_dirichlet_epsilon(
        self,
        progress: float,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
    ) -> None:
        """
        Update epsilon based on normalized training progress (0 => 1).
        """
        min_val = float(self._epsilon_min_value if min_value is None else min_value)
        max_val = float(self._epsilon_max_value if max_value is None else max_value)
        progress_tensor = tf.convert_to_tensor(float(progress), dtype=tf.float32)
        progress_tensor = tf.clip_by_value(progress_tensor, 0.0, 1.0)
        min_tensor = tf.constant(min_val, dtype=tf.float32)
        max_tensor = tf.constant(max_val, dtype=tf.float32)
        new_value = max_tensor * (1.0 - progress_tensor)
        new_value = tf.clip_by_value(new_value, min_tensor, max_tensor)
        
        # Also decay temperature if desired (optional future feature)
        self._dirichlet_epsilon.assign(new_value)

    def reset_dirichlet_epsilon(self) -> None:
        """Return epsilon to its starting value."""
        self._dirichlet_epsilon.assign(self._epsilon_max_value)

    def set_temperature(self, temperature: float) -> None:
        """Update the Dirichlet logit temperature at runtime (for schedule-driven annealing).

        Args:
            temperature: New temperature value. Values > 1 flatten the Dirichlet
                (encouraging diversity), values < 1 sharpen it (encouraging conviction).
        """
        self._logit_temperature = float(max(temperature, 1e-6))

    def set_alpha_cap(self, alpha_cap: float) -> None:
        """Update the Dirichlet alpha cap at runtime.

        Args:
            alpha_cap: New alpha cap value. Set to None to disable capping.
        """
        self._alpha_cap = float(alpha_cap) if alpha_cap is not None else None

    def _compute_alpha(self, logits: tf.Tensor) -> tf.Tensor:
        """
        Apply the selected activation to produce Dirichlet concentration parameters.
        Includes temperature scaling and optional capping.
        """
        logits = tf.convert_to_tensor(logits)
        eps = tf.cast(self.epsilon_value(), logits.dtype)
        activation = self._alpha_activation
        
        # 1. Apply Temperature Scaling (flatten logits before activation)
        if self._adaptive_temperature_enabled:
            abs_logits = tf.stop_gradient(tf.abs(logits))
            temp = (
                tf.cast(self._adaptive_temperature_base, logits.dtype)
                + tf.cast(self._adaptive_temperature_slope, logits.dtype) * abs_logits
            )
            temp = tf.clip_by_value(
                temp,
                tf.cast(self._adaptive_temperature_min, logits.dtype),
                tf.cast(self._adaptive_temperature_max, logits.dtype),
            )
            scaled_logits = logits / tf.maximum(temp, tf.cast(1e-6, logits.dtype))
        elif abs(self._logit_temperature - 1.0) > 1e-6:
            scaled_logits = logits / self._logit_temperature
        else:
            scaled_logits = logits

        # 2. Apply Activation (Shifted for Positivity)
        if activation == "elu":
            # ELU + 1 ensures strictly positive range (-1 -> 0)
            alpha = tf.nn.elu(scaled_logits) + 1.0 + eps
        elif activation == "softplus_shift":
            alpha = tf.nn.softplus(scaled_logits - 1.0) + 1.0 + eps
        elif activation == "swish":
            # Swish can be negative, so we must shift it too? 
            # Or assume user knows risks. Let's add +1 for safety similar to ELU.
            alpha = tf.nn.swish(scaled_logits) + 1.0 + eps
        elif activation == "mish":
            alpha = scaled_logits * tf.nn.tanh(tf.nn.softplus(scaled_logits)) + 1.0 + eps
        elif activation == "exp_clip":
            low, high = self._exp_clip
            alpha = tf.exp(tf.clip_by_value(scaled_logits, low, high)) + eps
        elif activation == "exp_tanh":
            # PERF-FIX #4c: exp(tanh(x) * scale) + eps
            # Bounded output prevents alpha explosion and naturally encourages
            # diversity. Configurable via dirichlet_exp_tanh_scale.
            # scale=2.5 -> range [0.08, 12.2], scale=3.5 -> range [0.03, 33.1]
            exp_tanh_scale = getattr(self, '_exp_tanh_scale', 2.5)
            alpha = tf.exp(tf.nn.tanh(scaled_logits) * exp_tanh_scale) + eps
        elif activation in {"cross_softplus", "cross_sectional_softplus", "cs_softplus"}:
            centered_logits = scaled_logits - tf.reduce_mean(scaled_logits, axis=-1, keepdims=True)
            if self._cross_sectional_standardize:
                centered_scale = tf.math.reduce_std(centered_logits, axis=-1, keepdims=True)
                centered_logits = centered_logits / tf.maximum(centered_scale, tf.cast(1e-6, centered_logits.dtype))
            alpha = (
                tf.cast(self._softplus_alpha_floor, centered_logits.dtype)
                + tf.nn.softplus(centered_logits * tf.cast(self._softplus_alpha_scale, centered_logits.dtype))
                + eps
            )
        else:
            # Default / legacy: softplus + adaptive epsilon
            alpha = tf.nn.softplus(scaled_logits) + eps

        # 3. Apply Alpha Cap (Safety Ceiling)
        if self._alpha_cap is not None:
            alpha_cap = tf.cast(self._alpha_cap, alpha.dtype)
            alpha = tf.minimum(alpha, alpha_cap)

        # Ensure strictly positive
        return tf.maximum(alpha, tf.cast(1e-6, alpha.dtype))

    def _format_actor_output(
        self,
        *,
        logits_for_alpha: tf.Tensor,
        mixture_logits_for_alpha: Optional[tf.Tensor] = None,
        mixture_gating_logits: Optional[tf.Tensor] = None,
        projection_logits: Optional[tf.Tensor] = None,
        aux_return_preds: Optional[tf.Tensor] = None,
    ):
        """Return backward-compatible actor outputs.

        Single-head mode returns alpha tensor (legacy behavior) UNLESS aux predictions
        are available, in which case a dict is returned.
        Dual-head mode returns dict with dirichlet alpha + softmax/projection logits.
        """
        proj_logits = logits_for_alpha if projection_logits is None else projection_logits
        alpha = self._compute_alpha(logits_for_alpha)
        if mixture_logits_for_alpha is not None:
            mixture_alpha = self._compute_alpha(mixture_logits_for_alpha)
            result = {
                "alpha": alpha,
                "mixture_alpha": mixture_alpha,
                "mixture_gating_logits": mixture_gating_logits,
                "projection_logits": proj_logits if self._dual_head_enabled else None,
            }
            if aux_return_preds is not None:
                result["aux_return_preds"] = aux_return_preds
            return result
        # If aux predictions exist OR dual-head is enabled, return structured dict
        if self._dual_head_enabled or aux_return_preds is not None:
            result = {
                "alpha": alpha,
                "projection_logits": proj_logits if self._dual_head_enabled else None,
            }
            if aux_return_preds is not None:
                result["aux_return_preds"] = aux_return_preds
            return result
        return alpha


class MLPActor(DirichletActor):
    """
    Windowed MLP actor.

    Consumes the same historical sequence window as the TCN variants, but
    flattens the full window and applies a dense backbone instead of temporal
    convolutions.
    """

    def __init__(
        self,
        input_dim: int,
        num_actions: int,
        sequence_length: int = 60,
        hidden_dims: Optional[List[int]] = None,
        dropout: Optional[float] = None,
        regime_conditioning_enabled: Optional[bool] = None,
        regime_conditioning_hidden_dim: Optional[int] = None,
        regime_conditioning_dropout: Optional[float] = None,
        regime_conditioning_mode: Optional[str] = None,
        name: str = "mlp_actor",
        epsilon_start: float = 0.5,
        epsilon_min: float = 0.1,
        alpha_activation: str = None,
        exp_clip: Tuple[float, float] = None,
        logit_temperature: float = None,
        alpha_cap: float = None,
        adaptive_temperature_enabled: bool = False,
        adaptive_temperature_base: float = 1.0,
        adaptive_temperature_slope: float = 0.0,
        adaptive_temperature_min: float = 0.8,
        adaptive_temperature_max: float = 2.5,
        dual_head_enabled: Optional[bool] = None,
        mixture_dirichlet_enabled: Optional[bool] = None,
        mixture_dirichlet_num_components: Optional[int] = None,
        mixture_dirichlet_gating_hidden_dims: Optional[List[int]] = None,
        mixture_dirichlet_component_hidden_dims: Optional[List[int]] = None,
        aux_return_enabled: bool = False,
        exp_tanh_scale: float = 2.5,
    ):
        if hidden_dims is None:
            hidden_dims = _DEFAULT_ACTOR_HIDDEN_DIMS
        if dropout is None:
            dropout = _DEFAULT_TCN_DROPOUT
        if regime_conditioning_enabled is None:
            regime_conditioning_enabled = _DEFAULT_REGIME_CONDITIONING_ENABLED
        if regime_conditioning_hidden_dim is None:
            regime_conditioning_hidden_dim = _DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM
        if regime_conditioning_dropout is None:
            regime_conditioning_dropout = _DEFAULT_REGIME_CONDITIONING_DROPOUT
        if dual_head_enabled is None:
            dual_head_enabled = _DEFAULT_DUAL_HEAD_ENABLED
        if mixture_dirichlet_enabled is None:
            mixture_dirichlet_enabled = _DEFAULT_MIXTURE_DIRICHLET_ENABLED
        if mixture_dirichlet_num_components is None:
            mixture_dirichlet_num_components = _DEFAULT_MIXTURE_DIRICHLET_COMPONENTS
        if mixture_dirichlet_gating_hidden_dims is None:
            mixture_dirichlet_gating_hidden_dims = _DEFAULT_MIXTURE_DIRICHLET_GATING_HIDDEN_DIMS
        if mixture_dirichlet_component_hidden_dims is None:
            mixture_dirichlet_component_hidden_dims = _DEFAULT_MIXTURE_DIRICHLET_COMPONENT_HIDDEN_DIMS

        super(MLPActor, self).__init__(
            name=name,
            epsilon_start=epsilon_start,
            epsilon_min=epsilon_min,
            alpha_activation=alpha_activation,
            exp_clip=exp_clip,
            logit_temperature=logit_temperature,
            alpha_cap=alpha_cap,
            adaptive_temperature_enabled=adaptive_temperature_enabled,
            adaptive_temperature_base=adaptive_temperature_base,
            adaptive_temperature_slope=adaptive_temperature_slope,
            adaptive_temperature_min=adaptive_temperature_min,
            adaptive_temperature_max=adaptive_temperature_max,
            dual_head_enabled=bool(dual_head_enabled),
            exp_tanh_scale=exp_tanh_scale,
        )

        sanitized_hidden_dims = [int(x) for x in (hidden_dims or []) if int(x) > 0]
        if not sanitized_hidden_dims:
            sanitized_hidden_dims = list(_DEFAULT_ACTOR_HIDDEN_DIMS)
        self.input_dim = int(input_dim)
        self.sequence_length = max(1, int(sequence_length))
        self.flat_dim = int(self.sequence_length * self.input_dim)
        self.num_actions = int(num_actions)
        self.latent_dim = int(sanitized_hidden_dims[-1])
        self.regime_conditioning_enabled = bool(regime_conditioning_enabled)
        self.regime_conditioning_mode = str(
            regime_conditioning_mode if regime_conditioning_mode is not None else _DEFAULT_REGIME_CONDITIONING_MODE
        ).lower().strip()

        self.sequence_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_sequence_norm")
        self.flatten_layer = layers.Reshape((self.flat_dim,), name=f"{name}_flatten")
        self.input_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_input_norm")
        self.hidden_layers: List[Tuple[layers.Dense, layers.Dropout]] = []
        for i, hidden_units in enumerate(sanitized_hidden_dims):
            self.hidden_layers.append(
                (
                    layers.Dense(hidden_units, activation="gelu", name=f"{name}_dense_{i}"),
                    layers.Dropout(float(dropout), name=f"{name}_dropout_{i}"),
                )
            )

        self.regime_encoder = None
        self.regime_film_layer = None
        self.regime_sequence_film_layer = None
        self.regime_fusion = None
        self.regime_dropout = None
        self.regime_sequence_encoder = None
        if self.regime_conditioning_enabled:
            (
                self.regime_sequence_encoder,
                self.regime_sequence_film_layer,
                self.regime_film_layer,
                self.regime_fusion,
                self.regime_dropout,
            ) = _build_regime_conditioning_modules(
                name=name,
                feature_dim=self.latent_dim,
                hidden_dim=max(8, int(regime_conditioning_hidden_dim)),
                dropout=float(max(0.0, regime_conditioning_dropout)),
                mode=self.regime_conditioning_mode,
                sequence_film_feature_dim=self.input_dim,
            )

        self.output_layer = layers.Dense(
            self.num_actions,
            activation=None,
            kernel_initializer="orthogonal",
            bias_initializer=tf.keras.initializers.Constant(0.5),
            name=f"{name}_output",
        )
        self.projection_layer = None
        if self._dual_head_enabled:
            self.projection_layer = layers.Dense(
                self.num_actions,
                activation=None,
                kernel_initializer="orthogonal",
                bias_initializer="zeros",
                name=f"{name}_projection",
            )

        self._aux_return_enabled = bool(aux_return_enabled)
        self.aux_return_head = None
        if self._aux_return_enabled:
            self.aux_return_head = tf.keras.Sequential(
                [
                    layers.Dense(max(32, self.latent_dim // 2), activation="relu", name=f"{name}_aux_h1"),
                    layers.Dropout(0.05),
                    layers.Dense(max(1, self.num_actions - 1), activation=None, name=f"{name}_aux_out"),
                ],
                name=f"{name}_aux_return_predictor",
            )

        self.mixture_dirichlet_enabled = bool(mixture_dirichlet_enabled)
        self.mixture_dirichlet_num_components = max(1, int(mixture_dirichlet_num_components))
        gating_dims = [int(x) for x in (mixture_dirichlet_gating_hidden_dims or []) if int(x) > 0]
        component_dims = [int(x) for x in (mixture_dirichlet_component_hidden_dims or []) if int(x) > 0]
        self.mixture_gating_layers: List[Tuple[layers.Dense, layers.Dropout]] = []
        self.mixture_component_layers: List[Tuple[layers.Dense, layers.Dropout]] = []
        self.mixture_component_norm = None
        self.mixture_gating_logits_layer = None
        self.mixture_output_layer = None
        if self.mixture_dirichlet_enabled:
            for i, hidden_units in enumerate(gating_dims):
                self.mixture_gating_layers.append(
                    (
                        layers.Dense(hidden_units, activation="gelu", name=f"{name}_mix_gate_{i}"),
                        layers.Dropout(float(dropout), name=f"{name}_mix_gate_drop_{i}"),
                    )
                )
            self.mixture_gating_logits_layer = layers.Dense(
                self.mixture_dirichlet_num_components,
                activation=None,
                kernel_initializer="orthogonal",
                bias_initializer="zeros",
                name=f"{name}_mixture_gating_logits",
            )
            if component_dims:
                self.mixture_component_norm = layers.LayerNormalization(
                    epsilon=1e-6, name=f"{name}_mixture_component_norm"
                )
                for i, hidden_units in enumerate(component_dims):
                    self.mixture_component_layers.append(
                        (
                            layers.Dense(hidden_units, activation="gelu", name=f"{name}_mix_comp_{i}"),
                            layers.Dropout(float(dropout), name=f"{name}_mix_comp_drop_{i}"),
                        )
                    )
            self.mixture_output_layer = layers.Dense(
                self.num_actions * self.mixture_dirichlet_num_components,
                activation=None,
                kernel_initializer="orthogonal",
                bias_initializer=tf.keras.initializers.Constant(0.5),
                name=f"{name}_mixture_output",
            )

    def _prepare_sequence(self, state) -> tf.Tensor:
        sequence = _flatten_structured_sequence_input(state)
        if sequence.shape.rank == 2:
            sequence = tf.expand_dims(sequence, axis=0)

        pad_time = tf.maximum(0, self.sequence_length - tf.shape(sequence)[1])
        sequence = tf.pad(sequence, [[0, 0], [0, pad_time], [0, 0]])
        sequence = sequence[:, : self.sequence_length, :]

        pad_feat = tf.maximum(0, self.input_dim - tf.shape(sequence)[2])
        sequence = tf.pad(sequence, [[0, 0], [0, 0], [0, pad_feat]])
        sequence = sequence[:, :, : self.input_dim]
        sequence = tf.ensure_shape(sequence, [None, self.sequence_length, self.input_dim])
        return sequence

    def call(self, state, training=None):
        sequence = self._prepare_sequence(state)
        regime_seq = sequence
        regime_embedding = None
        if self.regime_conditioning_enabled and self.regime_sequence_encoder is not None:
            regime_embedding = self.regime_sequence_encoder(regime_seq, training=training)

        sequence = self.sequence_norm(sequence)
        if self.regime_sequence_film_layer is not None and regime_embedding is not None:
            sequence = self.regime_sequence_film_layer(sequence, regime_embedding, training=training)
        x = self.flatten_layer(sequence)
        x = self.input_norm(x)
        for dense_layer, dropout_layer in self.hidden_layers:
            x = dense_layer(x)
            x = dropout_layer(x, training=training)

        if self.regime_conditioning_enabled and regime_embedding is not None:
            x = _apply_regime_conditioning(
                x,
                regime_embedding,
                regime_film_layer=self.regime_film_layer,
                regime_fusion=self.regime_fusion,
                regime_dropout=self.regime_dropout,
                training=training,
            )

        logits = self.output_layer(x, training=training)
        projection_logits = self.projection_layer(x, training=training) if self.projection_layer is not None else None
        aux_preds = self.aux_return_head(x, training=training) if self.aux_return_head is not None else None

        gating_logits = None
        mixture_logits = None
        if self.mixture_dirichlet_enabled and self.mixture_gating_logits_layer is not None:
            gating_features = x
            for dense_layer, dropout_layer in self.mixture_gating_layers:
                gating_features = dense_layer(gating_features)
                gating_features = dropout_layer(gating_features, training=training)
            gating_logits = self.mixture_gating_logits_layer(gating_features, training=training)

            component_features = x
            if self.mixture_component_norm is not None:
                component_features = self.mixture_component_norm(component_features)
            for dense_layer, dropout_layer in self.mixture_component_layers:
                component_features = dense_layer(component_features)
                component_features = dropout_layer(component_features, training=training)
            mixture_logits = self.mixture_output_layer(component_features, training=training)
            mixture_logits = tf.reshape(
                mixture_logits,
                (-1, self.mixture_dirichlet_num_components, self.num_actions),
            )

        return self._format_actor_output(
            logits_for_alpha=logits,
            mixture_logits_for_alpha=mixture_logits,
            mixture_gating_logits=gating_logits,
            projection_logits=projection_logits,
            aux_return_preds=aux_preds,
        )

    def get_film_diagnostics(self, state) -> Dict[str, float]:
        if not self.regime_conditioning_enabled or self.regime_sequence_encoder is None:
            return {}
        sequence = self._prepare_sequence(state)
        regime_embedding = self.regime_sequence_encoder(sequence, training=False)
        diagnostics: Dict[str, float] = {}
        if self.regime_sequence_film_layer is not None:
            for key, value in self.regime_sequence_film_layer.get_modulation_stats(regime_embedding).items():
                diagnostics[f"seq_{key}"] = value
        if self.regime_film_layer is not None:
            for key, value in self.regime_film_layer.get_modulation_stats(regime_embedding).items():
                diagnostics[f"latent_{key}"] = value
        return diagnostics


class TCNActor(DirichletActor):
    """
    Temporal Convolutional Network Actor.
    
    Uses dilated causal convolutions for efficient sequence processing.
    
    Input shape: (batch, timesteps, features)
    Output shape: (batch, num_actions) - Dirichlet alphas
    """
    
    def __init__(
        self,
        input_dim: int,
        num_actions: int,
        tcn_filters: List[int] = None,
        kernel_size: int = None,
        dilations: List[int] = None,
        dropout: float = None,
        recurrent_memory_enabled: Optional[bool] = None,
        recurrent_memory_units: Optional[int] = None,
        recurrent_memory_dropout: Optional[float] = None,
        regime_conditioning_enabled: Optional[bool] = None,
        regime_conditioning_hidden_dim: Optional[int] = None,
        regime_conditioning_dropout: Optional[float] = None,
        regime_conditioning_mode: Optional[str] = None,
        name: str = "tcn_actor",
        epsilon_start: float = 0.5,
        epsilon_min: float = 0.1,
        alpha_activation: str = None,
        exp_clip: Tuple[float, float] = None,
        logit_temperature: float = None,
        alpha_cap: float = None,
        adaptive_temperature_enabled: bool = False,
        adaptive_temperature_base: float = 1.0,
        adaptive_temperature_slope: float = 0.0,
        adaptive_temperature_min: float = 0.8,
        adaptive_temperature_max: float = 2.5,
        dual_head_enabled: Optional[bool] = None,
    ):
        # Apply config defaults
        if tcn_filters is None:
            tcn_filters = _DEFAULT_TCN_FILTERS
        if kernel_size is None:
            kernel_size = _DEFAULT_TCN_KERNEL_SIZE
        if dilations is None:
            dilations = _DEFAULT_TCN_DILATIONS
        if dropout is None:
            dropout = _DEFAULT_TCN_DROPOUT
        if recurrent_memory_enabled is None:
            recurrent_memory_enabled = _DEFAULT_RECURRENT_MEMORY_ENABLED
        if recurrent_memory_units is None:
            recurrent_memory_units = _DEFAULT_RECURRENT_MEMORY_UNITS
        if recurrent_memory_dropout is None:
            recurrent_memory_dropout = _DEFAULT_RECURRENT_MEMORY_DROPOUT
        if regime_conditioning_enabled is None:
            regime_conditioning_enabled = _DEFAULT_REGIME_CONDITIONING_ENABLED
        if regime_conditioning_hidden_dim is None:
            regime_conditioning_hidden_dim = _DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM
        if regime_conditioning_dropout is None:
            regime_conditioning_dropout = _DEFAULT_REGIME_CONDITIONING_DROPOUT
        if dual_head_enabled is None:
            dual_head_enabled = _DEFAULT_DUAL_HEAD_ENABLED
        
        super(TCNActor, self).__init__(
            name=name,
            epsilon_start=epsilon_start,
            epsilon_min=epsilon_min,
            alpha_activation=alpha_activation,
            exp_clip=exp_clip,
            logit_temperature=logit_temperature,
            alpha_cap=alpha_cap,
            adaptive_temperature_enabled=adaptive_temperature_enabled,
            adaptive_temperature_base=adaptive_temperature_base,
            adaptive_temperature_slope=adaptive_temperature_slope,
            adaptive_temperature_min=adaptive_temperature_min,
            adaptive_temperature_max=adaptive_temperature_max,
            dual_head_enabled=bool(dual_head_enabled),
        )
        
        self.input_dim = input_dim
        self.num_actions = num_actions
        self.recurrent_memory_enabled = bool(recurrent_memory_enabled)
        self.regime_conditioning_enabled = bool(regime_conditioning_enabled)
        self.regime_conditioning_mode = str(
            regime_conditioning_mode if regime_conditioning_mode is not None else _DEFAULT_REGIME_CONDITIONING_MODE
        ).lower().strip()
        
        # Build TCN blocks
        self.tcn_blocks = []
        for i, (filters, dilation) in enumerate(zip(tcn_filters, dilations)):
            self.tcn_blocks.append(
                TCNBlock(
                    filters=filters,
                    kernel_size=kernel_size,
                    dilation_rate=dilation,
                    dropout=dropout,
                    name=f'{name}_tcn_{i}'
                )
            )

        self.memory_layer = None
        if self.recurrent_memory_enabled:
            self.memory_layer = layers.LSTM(
                units=max(8, int(recurrent_memory_units)),
                return_sequences=True,
                dropout=float(max(0.0, recurrent_memory_dropout)),
                name=f"{name}_memory_lstm",
            )

        # Global pooling
        self.global_pool = layers.GlobalAveragePooling1D()
        self.regime_encoder = None
        self.regime_sequence_encoder = None
        self.regime_fusion = None
        self.regime_dropout = None
        self.regime_film_layer = None
        if self.regime_conditioning_enabled:
            (
                self.regime_sequence_encoder,
                _,
                self.regime_film_layer,
                self.regime_fusion,
                self.regime_dropout,
            ) = _build_regime_conditioning_modules(
                name=name,
                feature_dim=int(tcn_filters[-1]),
                hidden_dim=max(8, int(regime_conditioning_hidden_dim)),
                dropout=float(max(0.0, regime_conditioning_dropout)),
                mode=self.regime_conditioning_mode,
            )
        
        # Output layer
        self.output_layer = layers.Dense(
            num_actions,
            activation=None,
            kernel_initializer='orthogonal',
            bias_initializer=tf.keras.initializers.RandomNormal(mean=0.5, stddev=0.3),  # [HOT] FIX: Initialize away from zero
            name=f'{name}_output'
        )
        
    def call(self, state, training=None):
        """
        Args:
            state: (batch, timesteps, features)
            
        Returns:
            alpha: (batch, num_actions)
        """
        x = _flatten_structured_sequence_input(state)
        
        # TCN processing
        for block in self.tcn_blocks:
            x = block(x, training=training)

        if self.memory_layer is not None:
            x = self.memory_layer(x, training=training)

        regime_seq = x

        # x is now (batch, timesteps, tcn_filters[-1])

        # Aggregate sequence
        x = self.global_pool(x)  # (batch, tcn_filters[-1])

        if self.regime_conditioning_enabled and self.regime_sequence_encoder is not None:
            regime_embedding = self.regime_sequence_encoder(regime_seq, training=training)
            x = _apply_regime_conditioning(
                x,
                regime_embedding,
                regime_film_layer=self.regime_film_layer,
                regime_fusion=self.regime_fusion,
                regime_dropout=self.regime_dropout,
                training=training,
            )

        # Output
        logits = self.output_layer(x, training=training)
        return self._format_actor_output(logits_for_alpha=logits)


class TCNAttentionActor(DirichletActor):
    """
    TCN + Multi-Head Self-Attention Actor.
    
    Combines TCN's efficient convolutions with attention mechanism.
    
    Input shape: (batch, timesteps, features)
    Output shape: (batch, num_actions) - Dirichlet alphas
    """
    
    def __init__(
        self,
        input_dim: int,
        num_actions: int,
        tcn_filters: List[int] = None,
        kernel_size: int = None,
        dilations: List[int] = None,
        attention_heads: int = None,
        attention_dim: int = None,
        dropout: float = None,
        recurrent_memory_enabled: Optional[bool] = None,
        recurrent_memory_units: Optional[int] = None,
        recurrent_memory_dropout: Optional[float] = None,
        regime_conditioning_enabled: Optional[bool] = None,
        regime_conditioning_hidden_dim: Optional[int] = None,
        regime_conditioning_dropout: Optional[float] = None,
        regime_conditioning_mode: Optional[str] = None,
        name: str = "tcn_attention_actor",
        epsilon_start: float = 0.5,
        epsilon_min: float = 0.1,
        alpha_activation: str = None,
        exp_clip: Tuple[float, float] = None,
        logit_temperature: float = None,
        alpha_cap: float = None,
        adaptive_temperature_enabled: bool = False,
        adaptive_temperature_base: float = 1.0,
        adaptive_temperature_slope: float = 0.0,
        adaptive_temperature_min: float = 0.8,
        adaptive_temperature_max: float = 2.5,
        dual_head_enabled: Optional[bool] = None,
    ):
        # Apply config defaults
        if tcn_filters is None:
            tcn_filters = _DEFAULT_TCN_FILTERS
        if kernel_size is None:
            kernel_size = _DEFAULT_TCN_KERNEL_SIZE
        if dilations is None:
            dilations = _DEFAULT_TCN_DILATIONS
        if attention_heads is None:
            attention_heads = _DEFAULT_ATTENTION_HEADS
        if attention_dim is None:
            attention_dim = _DEFAULT_ATTENTION_DIM
        if dropout is None:
            dropout = _DEFAULT_TCN_DROPOUT
        if recurrent_memory_enabled is None:
            recurrent_memory_enabled = _DEFAULT_RECURRENT_MEMORY_ENABLED
        if recurrent_memory_units is None:
            recurrent_memory_units = _DEFAULT_RECURRENT_MEMORY_UNITS
        if recurrent_memory_dropout is None:
            recurrent_memory_dropout = _DEFAULT_RECURRENT_MEMORY_DROPOUT
        if regime_conditioning_enabled is None:
            regime_conditioning_enabled = _DEFAULT_REGIME_CONDITIONING_ENABLED
        if regime_conditioning_hidden_dim is None:
            regime_conditioning_hidden_dim = _DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM
        if regime_conditioning_dropout is None:
            regime_conditioning_dropout = _DEFAULT_REGIME_CONDITIONING_DROPOUT
        if dual_head_enabled is None:
            dual_head_enabled = _DEFAULT_DUAL_HEAD_ENABLED
        
        super(TCNAttentionActor, self).__init__(
            name=name,
            epsilon_start=epsilon_start,
            epsilon_min=epsilon_min,
            alpha_activation=alpha_activation,
            exp_clip=exp_clip,
            logit_temperature=logit_temperature,
            alpha_cap=alpha_cap,
            adaptive_temperature_enabled=adaptive_temperature_enabled,
            adaptive_temperature_base=adaptive_temperature_base,
            adaptive_temperature_slope=adaptive_temperature_slope,
            adaptive_temperature_min=adaptive_temperature_min,
            adaptive_temperature_max=adaptive_temperature_max,
            dual_head_enabled=bool(dual_head_enabled),
        )
        
        self.input_dim = input_dim
        self.num_actions = num_actions
        self.recurrent_memory_enabled = bool(recurrent_memory_enabled)
        self.regime_conditioning_enabled = bool(regime_conditioning_enabled)
        self.regime_conditioning_mode = str(
            regime_conditioning_mode if regime_conditioning_mode is not None else _DEFAULT_REGIME_CONDITIONING_MODE
        ).lower().strip()
        
        # TCN blocks
        self.tcn_blocks = []
        for i, (filters, dilation) in enumerate(zip(tcn_filters, dilations)):
            self.tcn_blocks.append(
                TCNBlock(
                    filters=filters,
                    kernel_size=kernel_size,
                    dilation_rate=dilation,
                    dropout=dropout,
                    name=f'{name}_tcn_{i}'
                )
            )
        
        # Project to attention dimension
        self.projection = layers.Dense(attention_dim, name=f'{name}_projection')
        
        # Attention
        self.attention = MultiHeadSelfAttention(
            d_model=attention_dim,
            num_heads=attention_heads,
            dropout=dropout,
            name=f'{name}_attention'
        )

        self.memory_layer = None
        if self.recurrent_memory_enabled:
            self.memory_layer = layers.LSTM(
                units=max(8, int(recurrent_memory_units)),
                return_sequences=True,
                dropout=float(max(0.0, recurrent_memory_dropout)),
                name=f"{name}_memory_lstm",
            )

        # Global pooling
        self.global_pool = layers.GlobalAveragePooling1D()
        self.regime_encoder = None
        self.regime_sequence_encoder = None
        self.regime_fusion = None
        self.regime_dropout = None
        self.regime_film_layer = None
        if self.regime_conditioning_enabled:
            (
                self.regime_sequence_encoder,
                _,
                self.regime_film_layer,
                self.regime_fusion,
                self.regime_dropout,
            ) = _build_regime_conditioning_modules(
                name=name,
                feature_dim=int(attention_dim),
                hidden_dim=max(8, int(regime_conditioning_hidden_dim)),
                dropout=float(max(0.0, regime_conditioning_dropout)),
                mode=self.regime_conditioning_mode,
            )
        
        # Output layer
        self.output_layer = layers.Dense(
            num_actions,
            activation=None,
            kernel_initializer='orthogonal',
            bias_initializer=tf.keras.initializers.Constant(0.5),  # [HOT] FIX: Initialize away from zero
            name=f'{name}_output'
        )
        
    def call(self, state, training=None):
        """
        Args:
            state: (batch, timesteps, features)
            
        Returns:
            alpha: (batch, num_actions)
        """
        x = _flatten_structured_sequence_input(state)
        
        # TCN processing
        for block in self.tcn_blocks:
            x = block(x, training=training)
        
        # Project to attention dimension
        x = self.projection(x)  # (batch, timesteps, attention_dim)
        
        # Apply attention
        x = self.attention(x, training=training)  # (batch, timesteps, attention_dim)

        if self.memory_layer is not None:
            x = self.memory_layer(x, training=training)

        regime_seq = x

        # Aggregate sequence
        x = self.global_pool(x)  # (batch, attention_dim)

        if self.regime_conditioning_enabled and self.regime_sequence_encoder is not None:
            regime_embedding = self.regime_sequence_encoder(regime_seq, training=training)
            x = _apply_regime_conditioning(
                x,
                regime_embedding,
                regime_film_layer=self.regime_film_layer,
                regime_fusion=self.regime_fusion,
                regime_dropout=self.regime_dropout,
                training=training,
            )

        # Output
        logits = self.output_layer(x, training=training)
        return self._format_actor_output(logits_for_alpha=logits)


class TCNFusionActor(DirichletActor):
    """
    Hierarchical fusion actor:
    - Per-asset temporal encoding (shared TCN encoder)
    - Cross-asset attention
    - Global context branch
    - Learnable gated fusion

    Input shape: (batch, timesteps, features)
    Output shape: (batch, num_actions) - Dirichlet alphas
    """

    def __init__(
        self,
        input_dim: int,
        num_actions: int,
        tcn_filters: List[int] = None,
        kernel_size: int = None,
        dilations: List[int] = None,
        dropout: float = None,
        num_assets: int = None,
        asset_feature_dim: int = None,
        global_feature_dim: int = None,
        fusion_embed_dim: int = None,
        fusion_attention_heads: int = None,
        fusion_dropout: float = None,
        fusion_cross_asset_mixer_enabled: Optional[bool] = None,
        fusion_cross_asset_mixer_layers: Optional[int] = None,
        fusion_cross_asset_mixer_expansion: Optional[float] = None,
        fusion_cross_asset_mixer_dropout: Optional[float] = None,
        fusion_alpha_head_hidden_dims: Optional[List[int]] = None,
        fusion_alpha_head_dropout: Optional[float] = None,
        fusion_asset_identity_enabled: Optional[bool] = None,
        fusion_context_cross_attention_enabled: Optional[bool] = None,
        fusion_context_cross_attention_heads: Optional[int] = None,
        fusion_context_cross_attention_dropout: Optional[float] = None,
        fusion_per_asset_alpha_head: Optional[bool] = None,
        recurrent_memory_enabled: Optional[bool] = None,
        recurrent_memory_units: Optional[int] = None,
        recurrent_memory_dropout: Optional[float] = None,
        regime_conditioning_enabled: Optional[bool] = None,
        regime_conditioning_hidden_dim: Optional[int] = None,
        regime_conditioning_dropout: Optional[float] = None,
        regime_conditioning_mode: Optional[str] = None,
        name: str = "tcn_fusion_actor",
        epsilon_start: float = 0.5,
        epsilon_min: float = 0.1,
        alpha_activation: str = None,
        exp_clip: Tuple[float, float] = None,
        logit_temperature: float = None,
        alpha_cap: float = None,
        adaptive_temperature_enabled: bool = False,
        adaptive_temperature_base: float = 1.0,
        adaptive_temperature_slope: float = 0.0,
        adaptive_temperature_min: float = 0.8,
        adaptive_temperature_max: float = 2.5,
        dual_head_enabled: Optional[bool] = None,
        mixture_dirichlet_enabled: Optional[bool] = None,
        mixture_dirichlet_num_components: Optional[int] = None,
        mixture_dirichlet_gating_hidden_dims: Optional[List[int]] = None,
        mixture_dirichlet_component_hidden_dims: Optional[List[int]] = None,
        aux_return_enabled: bool = False,
        exp_tanh_scale: float = 2.5,
    ):
        if tcn_filters is None:
            tcn_filters = _DEFAULT_TCN_FILTERS
        if kernel_size is None:
            kernel_size = _DEFAULT_TCN_KERNEL_SIZE
        if dilations is None:
            dilations = _DEFAULT_TCN_DILATIONS
        if dropout is None:
            dropout = _DEFAULT_TCN_DROPOUT
        if fusion_embed_dim is None:
            fusion_embed_dim = _DEFAULT_FUSION_EMBED_DIM
        if fusion_attention_heads is None:
            fusion_attention_heads = _DEFAULT_FUSION_HEADS
        if fusion_dropout is None:
            fusion_dropout = _DEFAULT_FUSION_DROPOUT
        if fusion_cross_asset_mixer_enabled is None:
            fusion_cross_asset_mixer_enabled = _DEFAULT_FUSION_CROSS_ASSET_MIXER_ENABLED
        if fusion_cross_asset_mixer_layers is None:
            fusion_cross_asset_mixer_layers = _DEFAULT_FUSION_CROSS_ASSET_MIXER_LAYERS
        if fusion_cross_asset_mixer_expansion is None:
            fusion_cross_asset_mixer_expansion = _DEFAULT_FUSION_CROSS_ASSET_MIXER_EXPANSION
        if fusion_cross_asset_mixer_dropout is None:
            fusion_cross_asset_mixer_dropout = _DEFAULT_FUSION_CROSS_ASSET_MIXER_DROPOUT
        if fusion_alpha_head_hidden_dims is None:
            fusion_alpha_head_hidden_dims = _DEFAULT_FUSION_ALPHA_HEAD_HIDDEN_DIMS
        if fusion_alpha_head_dropout is None:
            fusion_alpha_head_dropout = _DEFAULT_FUSION_ALPHA_HEAD_DROPOUT
        if fusion_asset_identity_enabled is None:
            fusion_asset_identity_enabled = _DEFAULT_FUSION_ASSET_IDENTITY_ENABLED
        if fusion_context_cross_attention_enabled is None:
            fusion_context_cross_attention_enabled = _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_ENABLED
        if fusion_context_cross_attention_heads is None:
            fusion_context_cross_attention_heads = _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_HEADS
        if fusion_context_cross_attention_dropout is None:
            fusion_context_cross_attention_dropout = _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_DROPOUT
        if fusion_per_asset_alpha_head is None:
            fusion_per_asset_alpha_head = _DEFAULT_FUSION_PER_ASSET_ALPHA_HEAD
        if recurrent_memory_enabled is None:
            recurrent_memory_enabled = _DEFAULT_RECURRENT_MEMORY_ENABLED
        if recurrent_memory_units is None:
            recurrent_memory_units = _DEFAULT_RECURRENT_MEMORY_UNITS
        if recurrent_memory_dropout is None:
            recurrent_memory_dropout = _DEFAULT_RECURRENT_MEMORY_DROPOUT
        if regime_conditioning_enabled is None:
            regime_conditioning_enabled = _DEFAULT_REGIME_CONDITIONING_ENABLED
        if regime_conditioning_hidden_dim is None:
            regime_conditioning_hidden_dim = _DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM
        if regime_conditioning_dropout is None:
            regime_conditioning_dropout = _DEFAULT_REGIME_CONDITIONING_DROPOUT
        if dual_head_enabled is None:
            dual_head_enabled = _DEFAULT_DUAL_HEAD_ENABLED
        if mixture_dirichlet_enabled is None:
            mixture_dirichlet_enabled = _DEFAULT_MIXTURE_DIRICHLET_ENABLED
        if mixture_dirichlet_num_components is None:
            mixture_dirichlet_num_components = _DEFAULT_MIXTURE_DIRICHLET_COMPONENTS
        if mixture_dirichlet_gating_hidden_dims is None:
            mixture_dirichlet_gating_hidden_dims = _DEFAULT_MIXTURE_DIRICHLET_GATING_HIDDEN_DIMS
        if mixture_dirichlet_component_hidden_dims is None:
            mixture_dirichlet_component_hidden_dims = _DEFAULT_MIXTURE_DIRICHLET_COMPONENT_HIDDEN_DIMS

        super(TCNFusionActor, self).__init__(
            name=name,
            epsilon_start=epsilon_start,
            epsilon_min=epsilon_min,
            alpha_activation=alpha_activation,
            exp_clip=exp_clip,
            logit_temperature=logit_temperature,
            alpha_cap=alpha_cap,
            adaptive_temperature_enabled=adaptive_temperature_enabled,
            adaptive_temperature_base=adaptive_temperature_base,
            adaptive_temperature_slope=adaptive_temperature_slope,
            adaptive_temperature_min=adaptive_temperature_min,
            adaptive_temperature_max=adaptive_temperature_max,
            dual_head_enabled=bool(dual_head_enabled),
            exp_tanh_scale=exp_tanh_scale,
        )

        self.input_dim = int(input_dim)
        self.num_actions = int(num_actions)
        self.num_assets = int(num_assets) if num_assets is not None else max(1, self.num_actions - 1)
        if asset_feature_dim is not None and int(asset_feature_dim) > 0:
            self.per_asset_dim = int(asset_feature_dim)
        else:
            self.per_asset_dim = int(np.ceil(self.input_dim / max(1, self.num_assets)))
        self.local_flat_dim = self.per_asset_dim * self.num_assets
        if global_feature_dim is not None:
            self.global_feature_dim = max(0, int(global_feature_dim))
        else:
            self.global_feature_dim = max(0, int(self.input_dim) - self.local_flat_dim)
        self.expected_input_dim = self.local_flat_dim + self.global_feature_dim
        self.fusion_embed_dim = int(fusion_embed_dim)
        self.recurrent_memory_enabled = bool(recurrent_memory_enabled)
        self.regime_conditioning_enabled = bool(regime_conditioning_enabled)

        if self.fusion_embed_dim % fusion_attention_heads != 0:
            fusion_attention_heads = 1
        self.fusion_attention_heads = int(fusion_attention_heads)

        self.asset_tcn_blocks = []
        for i, (filters, dilation) in enumerate(zip(tcn_filters, dilations)):
            self.asset_tcn_blocks.append(
                TCNBlock(
                    filters=filters,
                    kernel_size=kernel_size,
                    dilation_rate=dilation,
                    dropout=dropout,
                    name=f"{name}_asset_tcn_{i}",
                )
            )
        self.asset_memory_layer = None
        self.global_memory_layer = None
        if self.recurrent_memory_enabled:
            mem_units = max(8, int(recurrent_memory_units))
            mem_dropout = float(max(0.0, recurrent_memory_dropout))
            self.asset_memory_layer = layers.LSTM(
                units=mem_units,
                return_sequences=True,
                dropout=mem_dropout,
                name=f"{name}_asset_memory_lstm",
            )
            self.global_memory_layer = layers.LSTM(
                units=mem_units,
                return_sequences=True,
                dropout=mem_dropout,
                name=f"{name}_global_memory_lstm",
            )

        self.asset_time_pool = layers.GlobalAveragePooling1D()
        self.asset_projection = layers.Dense(self.fusion_embed_dim, activation="relu", name=f"{name}_asset_projection")
        self.asset_attention = MultiHeadSelfAttention(
            d_model=self.fusion_embed_dim,
            num_heads=self.fusion_attention_heads,
            dropout=fusion_dropout,
            name=f"{name}_asset_attention",
        )
        self.asset_mixer_blocks: List[CrossAssetMixerBlock] = []
        self.cross_asset_mixer_enabled = bool(fusion_cross_asset_mixer_enabled)
        if self.cross_asset_mixer_enabled:
            mixer_layers = max(1, int(fusion_cross_asset_mixer_layers))
            mixer_dropout = float(fusion_cross_asset_mixer_dropout)
            mixer_expansion = float(fusion_cross_asset_mixer_expansion)
            for i in range(mixer_layers):
                self.asset_mixer_blocks.append(
                    CrossAssetMixerBlock(
                        d_model=self.fusion_embed_dim,
                        num_heads=self.fusion_attention_heads,
                        expansion=mixer_expansion,
                        dropout=mixer_dropout,
                        name=f"{name}_asset_mixer_{i}",
                    )
                )

        # --- Cross-Asset Attention v2 upgrades ---

        # Change 1: Learnable asset identity embeddings
        self.asset_identity_enabled = bool(fusion_asset_identity_enabled)
        self.asset_identity_embed = None
        if self.asset_identity_enabled:
            self.asset_identity_embed = self.add_weight(
                name=f"{name}_asset_identity",
                shape=(self.num_assets, self.fusion_embed_dim),
                initializer=tf.keras.initializers.TruncatedNormal(stddev=0.02),
                trainable=True,
            )

        # Change 2: Context cross-attention (assets attend to global context)
        self.context_cross_attn_enabled = bool(fusion_context_cross_attention_enabled)
        self.context_cross_attn_block = None
        self.context_projection = None
        if self.context_cross_attn_enabled:
            ctx_heads = int(fusion_context_cross_attention_heads)
            ctx_dropout = float(fusion_context_cross_attention_dropout)
            self.context_cross_attn_block = ContextCrossAttentionBlock(
                d_model=self.fusion_embed_dim,
                num_heads=ctx_heads,
                expansion=2.0,
                dropout=ctx_dropout,
                name=f"{name}_ctx_cross_attn",
            )
            # Project global context to same embedding dim for cross-attention
            self.context_projection = layers.Dense(
                self.fusion_embed_dim, activation="relu",
                name=f"{name}_ctx_projection",
            )
        # 3-layer stack mode:
        # self-attn (mixer[0]) -> context cross-attn -> self-attn (mixer[1:]).
        self.use_three_layer_context_stack = bool(
            self.context_cross_attn_enabled
            and self.cross_asset_mixer_enabled
            and len(self.asset_mixer_blocks) >= 2
        )

        # Change 3: Per-asset alpha head (bypass AvgPool bottleneck)
        self.per_asset_alpha_head_enabled = bool(fusion_per_asset_alpha_head)
        self.asset_pool = layers.GlobalAveragePooling1D()  # kept as fallback

        self.global_time_pool = layers.GlobalAveragePooling1D()
        self.global_projection = layers.Dense(self.fusion_embed_dim, activation="relu", name=f"{name}_global_projection")
        self.global_dropout = layers.Dropout(fusion_dropout)

        # Gate layer for legacy path (used when context cross-attn is disabled)
        self.gate_layer = layers.Dense(self.fusion_embed_dim, activation="sigmoid", name=f"{name}_gate")
        self.regime_encoder = None
        self.regime_sequence_encoder = None
        self.regime_sequence_film_layer = None
        self.regime_context_sequence_film_layer = None
        self.regime_fusion = None
        self.regime_dropout = None
        self.regime_film_layer = None
        self.regime_conditioning_mode = 'concat'
        if self.regime_conditioning_enabled:
            rc_mode = str(regime_conditioning_mode) if regime_conditioning_mode else _DEFAULT_REGIME_CONDITIONING_MODE
            self.regime_conditioning_mode = str(rc_mode).lower().strip()
            (
                self.regime_sequence_encoder,
                self.regime_sequence_film_layer,
                self.regime_film_layer,
                self.regime_fusion,
                self.regime_dropout,
            ) = _build_regime_conditioning_modules(
                name=name,
                feature_dim=self.fusion_embed_dim,
                hidden_dim=max(8, int(regime_conditioning_hidden_dim)),
                dropout=float(max(0.0, regime_conditioning_dropout)),
                mode=self.regime_conditioning_mode,
                sequence_film_feature_dim=self.per_asset_dim,
                latent_gamma_limit=0.25,
                latent_beta_limit=0.15,
                sequence_gamma_limit=0.12,
                sequence_beta_limit=0.08,
            )
            if self.regime_conditioning_mode == "film" and self.global_feature_dim > 0:
                self.regime_context_sequence_film_layer = FiLMLayer(
                    feature_dim=self.global_feature_dim,
                    conditioning_dim=max(8, int(regime_conditioning_hidden_dim)),
                    hidden_dim=max(8, int(regime_conditioning_hidden_dim // 2) or 8),
                    dropout=0.0,
                    gamma_limit=0.12,
                    beta_limit=0.08,
                    name=f"{name}_regime_context_sequence_film",
                )

        # Market-relative FiLM: condition on each asset's relative strength vs peers
        # Conditioning signal = (asset_tcn_output - market_mean) + identity_embed
        # This changes with market state, enabling adaptive rotation.
        self.asset_film_layer = None
        if self.per_asset_alpha_head_enabled:
            # conditioning_dim = embed_dim (relative signal, optionally + identity)
            cond_dim = self.fusion_embed_dim
            self.asset_film_layer = FiLMLayer(
                feature_dim=self.fusion_embed_dim,
                conditioning_dim=cond_dim,
                hidden_dim=32,
                dropout=0.05,
                name=f"{name}_asset_film",
            )

        sanitized_alpha_head_dims = [int(x) for x in (fusion_alpha_head_hidden_dims or []) if int(x) > 0]
        self.use_richer_alpha_head = len(sanitized_alpha_head_dims) > 0
        self.alpha_pre_norm = None
        self.alpha_head_blocks: List[Tuple[layers.Dense, layers.Dropout]] = []
        if self.use_richer_alpha_head:
            self.alpha_pre_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_alpha_pre_norm")
            for i, hidden_units in enumerate(sanitized_alpha_head_dims):
                self.alpha_head_blocks.append(
                    (
                        layers.Dense(hidden_units, activation="gelu", name=f"{name}_alpha_head_{i}"),
                        layers.Dropout(float(fusion_alpha_head_dropout), name=f"{name}_alpha_dropout_{i}"),
                    )
                )

        if self.per_asset_alpha_head_enabled:
            # Per-asset output: Dense(1) per risky asset embedding + explicit cash logit.
            self.per_asset_pre_norm = layers.LayerNormalization(
                epsilon=1e-6, name=f"{name}_per_asset_pre_norm"
            )
            self.per_asset_logit_head = layers.Dense(
                1, activation=None,
                kernel_initializer="orthogonal",
                bias_initializer=tf.keras.initializers.Constant(0.5),
                name=f"{name}_per_asset_logit",
            )
            self.cash_logit_head = None
            if self.num_actions > self.num_assets:
                self.cash_logit_head = layers.Dense(
                    self.num_actions - self.num_assets,
                    activation=None,
                    kernel_initializer="orthogonal",
                    bias_initializer=tf.keras.initializers.Constant(0.5),
                    name=f"{name}_cash_logit",
                )
            # Legacy output layer still exists for backward compat loading
            self.output_layer = layers.Dense(
                self.num_actions, activation=None,
                kernel_initializer="orthogonal",
                bias_initializer=tf.keras.initializers.Constant(0.5),
                name=f"{name}_output",
            )
        else:
            self.per_asset_pre_norm = None
            self.per_asset_logit_head = None
            self.cash_logit_head = None
            self.output_layer = layers.Dense(
                self.num_actions,
                activation=None,
                kernel_initializer="orthogonal",
                bias_initializer=tf.keras.initializers.Constant(0.5),
                name=f"{name}_output",
            )

        # Optional per-asset return prediction head. Keep it config-gated so
        # callers that expect the legacy tensor actor output are unaffected when
        # the auxiliary loss is disabled.
        self._aux_return_enabled = bool(aux_return_enabled)
        self.aux_return_head = None
        if self._aux_return_enabled:
            self.aux_return_head = tf.keras.Sequential([
                layers.Dense(64, activation='relu', name=f'{name}_aux_ret_h1'),
                layers.Dropout(0.05),
                layers.Dense(1, activation=None, name=f'{name}_aux_ret_out'),
            ], name=f'{name}_aux_return_predictor')
        self.mixture_dirichlet_enabled = bool(mixture_dirichlet_enabled)
        self.mixture_dirichlet_num_components = max(1, int(mixture_dirichlet_num_components))
        gating_dims = [int(x) for x in (mixture_dirichlet_gating_hidden_dims or []) if int(x) > 0]
        component_dims = [int(x) for x in (mixture_dirichlet_component_hidden_dims or []) if int(x) > 0]
        self.mixture_gating_layers: List[Tuple[layers.Dense, layers.Dropout]] = []
        self.mixture_component_layers: List[Tuple[layers.Dense, layers.Dropout]] = []
        self.mixture_component_norm = None
        self.mixture_gating_logits_layer = None
        self.mixture_output_layer = None
        self.per_asset_component_logit_head = None
        self.cash_component_logit_head = None
        if self.mixture_dirichlet_enabled:
            for i, hidden_units in enumerate(gating_dims):
                self.mixture_gating_layers.append(
                    (
                        layers.Dense(hidden_units, activation="gelu", name=f"{name}_mix_gate_{i}"),
                        layers.Dropout(float(fusion_alpha_head_dropout), name=f"{name}_mix_gate_drop_{i}"),
                    )
                )
            self.mixture_gating_logits_layer = layers.Dense(
                self.mixture_dirichlet_num_components,
                activation=None,
                kernel_initializer="orthogonal",
                bias_initializer="zeros",
                name=f"{name}_mixture_gating_logits",
            )
            if component_dims:
                self.mixture_component_norm = layers.LayerNormalization(
                    epsilon=1e-6, name=f"{name}_mixture_component_norm"
                )
                for i, hidden_units in enumerate(component_dims):
                    self.mixture_component_layers.append(
                        (
                            layers.Dense(hidden_units, activation="gelu", name=f"{name}_mix_comp_{i}"),
                            layers.Dropout(float(fusion_alpha_head_dropout), name=f"{name}_mix_comp_drop_{i}"),
                        )
                    )
            if self.per_asset_alpha_head_enabled:
                self.per_asset_component_logit_head = layers.Dense(
                    self.mixture_dirichlet_num_components,
                    activation=None,
                    kernel_initializer="orthogonal",
                    bias_initializer=tf.keras.initializers.Constant(0.5),
                    name=f"{name}_per_asset_component_logit",
                )
                if self.num_actions > self.num_assets:
                    self.cash_component_logit_head = layers.Dense(
                        (self.num_actions - self.num_assets) * self.mixture_dirichlet_num_components,
                        activation=None,
                        kernel_initializer="orthogonal",
                        bias_initializer=tf.keras.initializers.Constant(0.5),
                        name=f"{name}_cash_component_logit",
                    )
            else:
                self.mixture_output_layer = layers.Dense(
                    self.num_actions * self.mixture_dirichlet_num_components,
                    activation=None,
                    kernel_initializer="orthogonal",
                    bias_initializer=tf.keras.initializers.Constant(0.5),
                    name=f"{name}_mixture_output",
                )

    def _align_feature_dim(self, x: tf.Tensor) -> tf.Tensor:
        """Pad/slice dynamic feature width so local/context split stays valid."""
        current_dim = tf.shape(x)[-1]
        pad_dim = tf.maximum(0, self.expected_input_dim - current_dim)
        x = tf.pad(x, [[0, 0], [0, 0], [0, pad_dim]])
        return x[:, :, : self.expected_input_dim]

    def _align_asset_tensor(self, asset_tensor: tf.Tensor) -> tf.Tensor:
        """Pad/slice asset and feature axes to deterministic fusion dimensions."""
        x_assets = _to_tensor_with_cast(asset_tensor, tf.float32)
        if x_assets.shape.rank != 4:
            raise ValueError(
                f"TCNFusionActor expects asset tensor rank=4 (batch,time,assets,features), got shape {x_assets.shape}"
            )

        pad_assets = tf.maximum(0, self.num_assets - tf.shape(x_assets)[2])
        x_assets = tf.pad(x_assets, [[0, 0], [0, 0], [0, pad_assets], [0, 0]])
        x_assets = x_assets[:, :, : self.num_assets, :]

        pad_feat = tf.maximum(0, self.per_asset_dim - tf.shape(x_assets)[-1])
        x_assets = tf.pad(x_assets, [[0, 0], [0, 0], [0, 0], [0, pad_feat]])
        x_assets = x_assets[:, :, :, : self.per_asset_dim]
        return x_assets

    def _align_context_tensor(
        self,
        context_tensor: tf.Tensor,
        *,
        batch: tf.Tensor,
        timesteps: tf.Tensor,
        fallback: tf.Tensor,
    ) -> tf.Tensor:
        """Pad/slice context tensor to (batch, timesteps, global_feature_dim)."""
        target_dim = int(self.global_feature_dim)
        if target_dim <= 0:
            return fallback

        if context_tensor is None:
            return tf.zeros((batch, timesteps, target_dim), dtype=fallback.dtype)

        context = _to_tensor_with_cast(context_tensor, fallback.dtype)
        if context.shape.rank == 2:
            context = tf.expand_dims(context, axis=1)
        elif context.shape.rank != 3:
            raise ValueError(
                f"TCNFusionActor expects context rank=2 or 3, got shape {context.shape}"
            )

        pad_time = tf.maximum(0, timesteps - tf.shape(context)[1])
        context = tf.pad(context, [[0, 0], [0, pad_time], [0, 0]])
        context = context[:, :timesteps, :]

        pad_dim = tf.maximum(0, target_dim - tf.shape(context)[-1])
        context = tf.pad(context, [[0, 0], [0, 0], [0, pad_dim]])
        context = context[:, :, :target_dim]
        return context

    def _build_regime_sequence(self, state) -> tf.Tensor:
        if isinstance(state, dict):
            structured_assets = self._align_asset_tensor(state.get("asset"))
            batch = tf.shape(structured_assets)[0]
            timesteps = tf.shape(structured_assets)[1]
            context_seq = self._align_context_tensor(
                state.get("context"),
                batch=batch,
                timesteps=timesteps,
                fallback=tf.zeros((batch, timesteps, self.per_asset_dim), dtype=structured_assets.dtype),
            )
            asset_flat_for_regime = tf.reshape(
                structured_assets,
                (batch, timesteps, self.num_assets * self.per_asset_dim),
            )
            return tf.concat([asset_flat_for_regime, context_seq], axis=-1)

        x = self._align_feature_dim(state)
        return x

    def call(self, state, training=None):
        if isinstance(state, dict):
            structured_assets = self._align_asset_tensor(state.get("asset"))
            batch = tf.shape(structured_assets)[0]
            timesteps = tf.shape(structured_assets)[1]
            x_assets = tf.transpose(structured_assets, perm=[0, 2, 1, 3])
            x_assets = tf.reshape(x_assets, (-1, timesteps, self.per_asset_dim))

            context_seq = self._align_context_tensor(
                state.get("context"),
                batch=batch,
                timesteps=timesteps,
                fallback=tf.zeros((batch, timesteps, self.per_asset_dim), dtype=structured_assets.dtype),
            )
            asset_flat_for_regime = tf.reshape(
                structured_assets,
                (batch, timesteps, self.num_assets * self.per_asset_dim),
            )
        else:
            x = self._align_feature_dim(state)
            batch = tf.shape(x)[0]
            timesteps = tf.shape(x)[1]
            x_local = x[:, :, : self.local_flat_dim]

            # (batch, timesteps, local_flat_dim) -> (batch*num_assets, timesteps, per_asset_dim)
            x_assets = tf.reshape(x_local, (batch, timesteps, self.num_assets, self.per_asset_dim))
            x_assets = tf.transpose(x_assets, perm=[0, 2, 1, 3])
            x_assets = tf.reshape(x_assets, (-1, timesteps, self.per_asset_dim))

            x_context = x[:, :, self.local_flat_dim:]
            if self.global_feature_dim <= 0:
                context_seq = x_local
            else:
                context_seq = self._align_context_tensor(
                    x_context,
                    batch=batch,
                    timesteps=timesteps,
                    fallback=x_local,
                )

        regime_embedding = None
        if self.regime_conditioning_enabled and self.regime_sequence_encoder is not None:
            regime_seq = self._build_regime_sequence(state)
            regime_embedding = self.regime_sequence_encoder(regime_seq, training=training)

        if regime_embedding is not None and self.regime_sequence_film_layer is not None:
            asset_regime_embedding = tf.repeat(regime_embedding, repeats=self.num_assets, axis=0)
            x_assets = self.regime_sequence_film_layer(x_assets, asset_regime_embedding, training=training)
        if regime_embedding is not None and self.regime_context_sequence_film_layer is not None:
            context_seq = self.regime_context_sequence_film_layer(context_seq, regime_embedding, training=training)

        # --- Per-asset TCN encoding (shared weights) ---
        for block in self.asset_tcn_blocks:
            x_assets = block(x_assets, training=training)
        if self.asset_memory_layer is not None:
            x_assets = self.asset_memory_layer(x_assets, training=training)

        x_assets = self.asset_time_pool(x_assets)
        x_assets = self.asset_projection(x_assets)
        x_assets = tf.reshape(x_assets, (batch, self.num_assets, self.fusion_embed_dim))

        # --- Change 1: Add asset identity embeddings ---
        if self.asset_identity_embed is not None:
            x_assets = x_assets + self.asset_identity_embed[tf.newaxis, :, :]

        # --- Cross-asset attention stack ---
        # Preferred v2 layout when enabled:
        #   layer1 self-attn (mixer[0]) -> layer2 context cross-attn -> layer3 self-attn (mixer[1:])
        if self.use_three_layer_context_stack:
            x_assets = self.asset_mixer_blocks[0](x_assets, training=training)
        else:
            x_assets = self.asset_attention(x_assets, training=training)
            for mixer_block in self.asset_mixer_blocks:
                x_assets = mixer_block(x_assets, training=training)

        # --- Global context branch ---
        if self.global_memory_layer is not None:
            context_seq = self.global_memory_layer(context_seq, training=training)
        global_context = self.global_time_pool(context_seq)
        global_context = self.global_projection(global_context)
        global_context = self.global_dropout(global_context, training=training)

        # --- Change 2: Context cross-attention OR legacy gate fusion ---
        if self.context_cross_attn_enabled and self.context_cross_attn_block is not None:
            # Project global context and reshape to (batch, 1, embed_dim) token
            ctx_token = self.context_projection(global_context)  # (batch, embed_dim)
            ctx_token = tf.expand_dims(ctx_token, axis=1)  # (batch, 1, embed_dim)
            # Assets attend to context: each asset queries the global context
            x_assets = self.context_cross_attn_block(
                query=x_assets,   # (batch, num_assets, embed_dim)
                context=ctx_token, # (batch, 1, embed_dim)
                training=training,
            )  # (batch, num_assets, embed_dim) — context-enriched
            if self.use_three_layer_context_stack:
                for mixer_block in self.asset_mixer_blocks[1:]:
                    x_assets = mixer_block(x_assets, training=training)
            # Keep a pooled fallback path valid when per-asset head is disabled.
            fused = self.asset_pool(x_assets)
        else:
            # Legacy: pool assets => gate with global => single fused vector
            asset_context = self.asset_pool(x_assets)
            gate = self.gate_layer(tf.concat([asset_context, global_context], axis=-1))
            fused = gate * asset_context + (1.0 - gate) * global_context

        # --- Regime conditioning ---
        if regime_embedding is not None:
            if self.per_asset_alpha_head_enabled:
                x_assets = _apply_regime_conditioning(
                    x_assets,
                    regime_embedding,
                    regime_film_layer=self.regime_film_layer,
                    regime_fusion=self.regime_fusion,
                    regime_dropout=self.regime_dropout,
                    training=training,
                )
            else:
                fused = _apply_regime_conditioning(
                    fused,
                    regime_embedding,
                    regime_film_layer=self.regime_film_layer,
                    regime_fusion=self.regime_fusion,
                    regime_dropout=self.regime_dropout,
                    training=training,
                )

        # --- Market-relative FiLM: condition on relative strength vs peers ---
        if self.asset_film_layer is not None:
            batch_size = tf.shape(x_assets)[0]
            # Relative signal: how each asset compares to the market average
            market_mean = tf.reduce_mean(x_assets, axis=1, keepdims=True)  # (batch, 1, embed)
            relative = x_assets - market_mean  # (batch, num_assets, embed) — changes with market
            # Add identity embedding if available (knows WHO + HOW it's doing)
            if self.asset_identity_embed is not None:
                identity = tf.tile(self.asset_identity_embed[tf.newaxis, :, :], [batch_size, 1, 1])
                relative = relative + identity
            x_flat = tf.reshape(x_assets, (-1, self.fusion_embed_dim))
            cond_flat = tf.reshape(relative, (-1, self.fusion_embed_dim))
            x_flat = self.asset_film_layer(x_flat, cond_flat, training=training)
            x_assets = tf.reshape(x_flat, (batch_size, self.num_assets, self.fusion_embed_dim))

        # --- SOTA-FIX Phase 3: Auxiliary per-asset return prediction ---
        # Branch off backbone features BEFORE the alpha head transforms them.
        # x_assets is (batch, num_assets, embed_dim) after cross-asset attention.
        aux_preds = None
        if self._aux_return_enabled and hasattr(self, 'aux_return_head'):
            # Predict per-asset returns: (batch, num_assets, embed) -> (batch, num_assets, 1) -> (batch, num_assets)
            aux_preds = self.aux_return_head(tf.stop_gradient(x_assets) if not training else x_assets, training=training)
            aux_preds = tf.squeeze(aux_preds, axis=-1)  # (batch, num_assets)

        # --- Change 3: Per-asset alpha head OR legacy pooled head ---
        if self.per_asset_alpha_head_enabled and self.per_asset_logit_head is not None:
            # x_assets is (batch, num_assets, embed_dim)
            # Apply optional richer alpha MLP per-asset
            if self.use_richer_alpha_head and self.alpha_pre_norm is not None:
                x_assets = self.alpha_pre_norm(x_assets)
                for dense_layer, dropout_layer in self.alpha_head_blocks:
                    x_assets = dense_layer(x_assets)
                    x_assets = dropout_layer(x_assets, training=training)
            else:
                x_assets = self.per_asset_pre_norm(x_assets)
            # Risky-asset logits: (batch, num_assets, embed_dim) => (batch, num_assets)
            risky_logits = self.per_asset_logit_head(x_assets, training=training)
            risky_logits = tf.squeeze(risky_logits, axis=-1)

            if self.cash_logit_head is not None:
                if self.use_richer_alpha_head and self.alpha_pre_norm is not None:
                    cash_features = self.alpha_pre_norm(fused)
                    for dense_layer, dropout_layer in self.alpha_head_blocks:
                        cash_features = dense_layer(cash_features)
                        cash_features = dropout_layer(cash_features, training=training)
                else:
                    cash_features = fused
                cash_logits = self.cash_logit_head(cash_features, training=training)
                logits = tf.concat([risky_logits, cash_logits], axis=-1)
            else:
                logits = risky_logits
        else:
            # Legacy path: single fused vector => Dense(num_actions)
            if self.use_richer_alpha_head and self.alpha_pre_norm is not None:
                alpha_features = self.alpha_pre_norm(fused)
                for dense_layer, dropout_layer in self.alpha_head_blocks:
                    alpha_features = dense_layer(alpha_features)
                    alpha_features = dropout_layer(alpha_features, training=training)
            else:
                alpha_features = fused
            logits = self.output_layer(alpha_features, training=training)

        gating_logits = None
        mixture_logits = None
        if self.mixture_dirichlet_enabled and self.mixture_gating_logits_layer is not None:
            gating_features = fused
            for dense_layer, dropout_layer in self.mixture_gating_layers:
                gating_features = dense_layer(gating_features)
                gating_features = dropout_layer(gating_features, training=training)
            gating_logits = self.mixture_gating_logits_layer(gating_features, training=training)

            if self.per_asset_alpha_head_enabled and self.per_asset_component_logit_head is not None:
                component_features = x_assets
                if self.mixture_component_norm is not None:
                    component_features = self.mixture_component_norm(component_features)
                for dense_layer, dropout_layer in self.mixture_component_layers:
                    component_features = dense_layer(component_features)
                    component_features = dropout_layer(component_features, training=training)
                risky_component_logits = self.per_asset_component_logit_head(component_features, training=training)
                risky_component_logits = tf.transpose(risky_component_logits, perm=[0, 2, 1])
                if self.cash_component_logit_head is not None:
                    cash_component_logits = self.cash_component_logit_head(fused, training=training)
                    cash_component_logits = tf.reshape(
                        cash_component_logits,
                        (-1, self.mixture_dirichlet_num_components, self.num_actions - self.num_assets),
                    )
                    mixture_logits = tf.concat([risky_component_logits, cash_component_logits], axis=-1)
                else:
                    mixture_logits = risky_component_logits
            else:
                component_features = alpha_features if 'alpha_features' in locals() else fused
                if self.mixture_component_norm is not None:
                    component_features = self.mixture_component_norm(component_features)
                for dense_layer, dropout_layer in self.mixture_component_layers:
                    component_features = dense_layer(component_features)
                    component_features = dropout_layer(component_features, training=training)
                mixture_logits = self.mixture_output_layer(component_features, training=training)
                mixture_logits = tf.reshape(
                    mixture_logits,
                    (-1, self.mixture_dirichlet_num_components, self.num_actions),
                )

        return self._format_actor_output(
            logits_for_alpha=logits,
            mixture_logits_for_alpha=mixture_logits,
            mixture_gating_logits=gating_logits,
            aux_return_preds=aux_preds,
        )

    def get_film_diagnostics(self, state) -> Dict[str, float]:
        diagnostics: Dict[str, float] = {}
        need_refresh = False
        for film_layer in (
            self.regime_sequence_film_layer,
            self.regime_context_sequence_film_layer,
            self.regime_film_layer,
            self.asset_film_layer,
        ):
            if film_layer is not None and not film_layer.get_last_modulation_stats():
                need_refresh = True
                break
        if need_refresh:
            try:
                _ = self(state, training=False)
            except Exception:
                return diagnostics

        seq_stats = _merge_modulation_stats(
            self.regime_sequence_film_layer.get_last_modulation_stats()
            if self.regime_sequence_film_layer is not None else {},
            self.regime_context_sequence_film_layer.get_last_modulation_stats()
            if self.regime_context_sequence_film_layer is not None else {},
        )
        diagnostics.update(_prefix_modulation_stats("seq", seq_stats))
        latent_stats = self.regime_film_layer.get_last_modulation_stats() if self.regime_film_layer is not None else {}
        diagnostics.update(_prefix_modulation_stats("latent", latent_stats))
        asset_stats = self.asset_film_layer.get_last_modulation_stats() if self.asset_film_layer is not None else {}
        diagnostics.update(_prefix_modulation_stats("asset", asset_stats))
        return diagnostics


# ============================================================================
# CRITIC NETWORKS
# ============================================================================

class TCNCritic(Model):
    """
    TCN-based Critic.
    
    Input shape: (batch, timesteps, features)
    Output shape: (batch, 1) - State value
    """
    
    def __init__(self,
                 input_dim: int,
                 tcn_filters: List[int] = None,
                 kernel_size: int = None,
                 dilations: List[int] = None,
                 dropout: float = None,
                 recurrent_memory_enabled: Optional[bool] = None,
                 recurrent_memory_units: Optional[int] = None,
                 recurrent_memory_dropout: Optional[float] = None,
                 regime_conditioning_enabled: Optional[bool] = None,
                 regime_conditioning_hidden_dim: Optional[int] = None,
                 regime_conditioning_dropout: Optional[float] = None,
                 regime_conditioning_mode: Optional[str] = None,
                 distributional_critic_enabled: Optional[bool] = None,
                 distributional_num_quantiles: Optional[int] = None,
                 name: str = "tcn_critic"):
        super(TCNCritic, self).__init__(name=name)
        
        # Apply config defaults
        if tcn_filters is None:
            tcn_filters = _DEFAULT_TCN_FILTERS
        if kernel_size is None:
            kernel_size = _DEFAULT_TCN_KERNEL_SIZE
        if dilations is None:
            dilations = _DEFAULT_TCN_DILATIONS
        if dropout is None:
            dropout = _DEFAULT_TCN_DROPOUT
        if recurrent_memory_enabled is None:
            recurrent_memory_enabled = _DEFAULT_RECURRENT_MEMORY_ENABLED
        if recurrent_memory_units is None:
            recurrent_memory_units = _DEFAULT_RECURRENT_MEMORY_UNITS
        if recurrent_memory_dropout is None:
            recurrent_memory_dropout = _DEFAULT_RECURRENT_MEMORY_DROPOUT
        if regime_conditioning_enabled is None:
            regime_conditioning_enabled = _DEFAULT_REGIME_CONDITIONING_ENABLED
        if regime_conditioning_hidden_dim is None:
            regime_conditioning_hidden_dim = _DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM
        if regime_conditioning_dropout is None:
            regime_conditioning_dropout = _DEFAULT_REGIME_CONDITIONING_DROPOUT
        if distributional_critic_enabled is None:
            distributional_critic_enabled = _DEFAULT_DISTRIBUTIONAL_CRITIC_ENABLED
        if distributional_num_quantiles is None:
            distributional_num_quantiles = _DEFAULT_DISTRIBUTIONAL_NUM_QUANTILES

        self.input_dim = input_dim
        self.recurrent_memory_enabled = bool(recurrent_memory_enabled)
        self.regime_conditioning_enabled = bool(regime_conditioning_enabled)
        self.regime_conditioning_mode = str(
            regime_conditioning_mode if regime_conditioning_mode is not None else _DEFAULT_REGIME_CONDITIONING_MODE
        ).lower().strip()
        self.distributional_critic_enabled = bool(distributional_critic_enabled)
        self.distributional_num_quantiles = max(2, int(distributional_num_quantiles))
        
        # TCN blocks
        self.tcn_blocks = []
        for i, (filters, dilation) in enumerate(zip(tcn_filters, dilations)):
            self.tcn_blocks.append(
                TCNBlock(
                    filters=filters,
                    kernel_size=kernel_size,
                    dilation_rate=dilation,
                    dropout=dropout,
                    name=f'{name}_tcn_{i}'
                )
            )

        self.memory_layer = None
        if self.recurrent_memory_enabled:
            self.memory_layer = layers.LSTM(
                units=max(8, int(recurrent_memory_units)),
                return_sequences=True,
                dropout=float(max(0.0, recurrent_memory_dropout)),
                name=f"{name}_memory_lstm",
            )

        # Global pooling
        self.global_pool = layers.GlobalAveragePooling1D()
        self.regime_encoder = None
        self.regime_sequence_encoder = None
        self.regime_fusion = None
        self.regime_dropout = None
        self.regime_film_layer = None
        if self.regime_conditioning_enabled:
            (
                self.regime_sequence_encoder,
                _,
                self.regime_film_layer,
                self.regime_fusion,
                self.regime_dropout,
            ) = _build_regime_conditioning_modules(
                name=name,
                feature_dim=int(tcn_filters[-1]),
                hidden_dim=max(8, int(regime_conditioning_hidden_dim)),
                dropout=float(max(0.0, regime_conditioning_dropout)),
                mode=self.regime_conditioning_mode,
            )

        output_units = self.distributional_num_quantiles if self.distributional_critic_enabled else 1

        # Output layer
        self.output_layer = layers.Dense(
            output_units,
            activation=None,
            kernel_initializer='orthogonal',
            name=f'{name}_output'
        )
    
    def call(self, state, training=None):
        """
        Args:
            state: (batch, timesteps, features)
            
        Returns:
            value: (batch, 1)
        """
        x = _flatten_structured_sequence_input(state)
        
        for block in self.tcn_blocks:
            x = block(x, training=training)

        if self.memory_layer is not None:
            x = self.memory_layer(x, training=training)

        regime_seq = x

        x = self.global_pool(x)
        if self.regime_conditioning_enabled and self.regime_sequence_encoder is not None:
            regime_embedding = self.regime_sequence_encoder(regime_seq, training=training)
            x = _apply_regime_conditioning(
                x,
                regime_embedding,
                regime_film_layer=self.regime_film_layer,
                regime_fusion=self.regime_fusion,
                regime_dropout=self.regime_dropout,
                training=training,
            )
        value = self.output_layer(x, training=training)

        return value


class MLPCritic(Model):
    """
    Windowed MLP critic that flattens the full sequence window and predicts a
    scalar value or quantile distribution.
    """

    def __init__(
        self,
        input_dim: int,
        sequence_length: int = 60,
        hidden_dims: Optional[List[int]] = None,
        dropout: Optional[float] = None,
        regime_conditioning_enabled: Optional[bool] = None,
        regime_conditioning_hidden_dim: Optional[int] = None,
        regime_conditioning_dropout: Optional[float] = None,
        regime_conditioning_mode: Optional[str] = None,
        distributional_critic_enabled: Optional[bool] = None,
        distributional_num_quantiles: Optional[int] = None,
        name: str = "mlp_critic",
    ):
        super(MLPCritic, self).__init__(name=name)

        if hidden_dims is None:
            hidden_dims = _DEFAULT_CRITIC_HIDDEN_DIMS
        if dropout is None:
            dropout = _DEFAULT_TCN_DROPOUT
        if regime_conditioning_enabled is None:
            regime_conditioning_enabled = _DEFAULT_REGIME_CONDITIONING_ENABLED
        if regime_conditioning_hidden_dim is None:
            regime_conditioning_hidden_dim = _DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM
        if regime_conditioning_dropout is None:
            regime_conditioning_dropout = _DEFAULT_REGIME_CONDITIONING_DROPOUT
        if distributional_critic_enabled is None:
            distributional_critic_enabled = _DEFAULT_DISTRIBUTIONAL_CRITIC_ENABLED
        if distributional_num_quantiles is None:
            distributional_num_quantiles = _DEFAULT_DISTRIBUTIONAL_NUM_QUANTILES

        sanitized_hidden_dims = [int(x) for x in (hidden_dims or []) if int(x) > 0]
        if not sanitized_hidden_dims:
            sanitized_hidden_dims = list(_DEFAULT_CRITIC_HIDDEN_DIMS)
        self.input_dim = int(input_dim)
        self.sequence_length = max(1, int(sequence_length))
        self.flat_dim = int(self.sequence_length * self.input_dim)
        self.latent_dim = int(sanitized_hidden_dims[-1])
        self.regime_conditioning_enabled = bool(regime_conditioning_enabled)
        self.regime_conditioning_mode = str(
            regime_conditioning_mode if regime_conditioning_mode is not None else _DEFAULT_REGIME_CONDITIONING_MODE
        ).lower().strip()
        self.distributional_critic_enabled = bool(distributional_critic_enabled)
        self.distributional_num_quantiles = max(2, int(distributional_num_quantiles))

        self.sequence_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_sequence_norm")
        self.flatten_layer = layers.Reshape((self.flat_dim,), name=f"{name}_flatten")
        self.input_norm = layers.LayerNormalization(epsilon=1e-6, name=f"{name}_input_norm")
        self.hidden_layers: List[Tuple[layers.Dense, layers.Dropout]] = []
        for i, hidden_units in enumerate(sanitized_hidden_dims):
            self.hidden_layers.append(
                (
                    layers.Dense(hidden_units, activation="gelu", name=f"{name}_dense_{i}"),
                    layers.Dropout(float(dropout), name=f"{name}_dropout_{i}"),
                )
            )

        self.regime_encoder = None
        self.regime_film_layer = None
        self.regime_sequence_film_layer = None
        self.regime_fusion = None
        self.regime_dropout = None
        self.regime_sequence_encoder = None
        if self.regime_conditioning_enabled:
            (
                self.regime_sequence_encoder,
                self.regime_sequence_film_layer,
                self.regime_film_layer,
                self.regime_fusion,
                self.regime_dropout,
            ) = _build_regime_conditioning_modules(
                name=name,
                feature_dim=self.latent_dim,
                hidden_dim=max(8, int(regime_conditioning_hidden_dim)),
                dropout=float(max(0.0, regime_conditioning_dropout)),
                mode=self.regime_conditioning_mode,
                sequence_film_feature_dim=self.input_dim,
            )

        output_units = self.distributional_num_quantiles if self.distributional_critic_enabled else 1
        self.output_layer = layers.Dense(
            output_units,
            activation=None,
            kernel_initializer="orthogonal",
            name=f"{name}_output",
        )

    def _prepare_sequence(self, state) -> tf.Tensor:
        sequence = _flatten_structured_sequence_input(state)
        if sequence.shape.rank == 2:
            sequence = tf.expand_dims(sequence, axis=0)

        pad_time = tf.maximum(0, self.sequence_length - tf.shape(sequence)[1])
        sequence = tf.pad(sequence, [[0, 0], [0, pad_time], [0, 0]])
        sequence = sequence[:, : self.sequence_length, :]

        pad_feat = tf.maximum(0, self.input_dim - tf.shape(sequence)[2])
        sequence = tf.pad(sequence, [[0, 0], [0, 0], [0, pad_feat]])
        sequence = sequence[:, :, : self.input_dim]
        sequence = tf.ensure_shape(sequence, [None, self.sequence_length, self.input_dim])
        return sequence

    def call(self, state, training=None):
        sequence = self._prepare_sequence(state)
        regime_seq = sequence
        regime_embedding = None
        if self.regime_conditioning_enabled and self.regime_sequence_encoder is not None:
            regime_embedding = self.regime_sequence_encoder(regime_seq, training=training)

        sequence = self.sequence_norm(sequence)
        if self.regime_sequence_film_layer is not None and regime_embedding is not None:
            sequence = self.regime_sequence_film_layer(sequence, regime_embedding, training=training)
        x = self.flatten_layer(sequence)
        x = self.input_norm(x)
        for dense_layer, dropout_layer in self.hidden_layers:
            x = dense_layer(x)
            x = dropout_layer(x, training=training)

        if self.regime_conditioning_enabled and regime_embedding is not None:
            x = _apply_regime_conditioning(
                x,
                regime_embedding,
                regime_film_layer=self.regime_film_layer,
                regime_fusion=self.regime_fusion,
                regime_dropout=self.regime_dropout,
                training=training,
            )

        return self.output_layer(x, training=training)


class TCNAttentionCritic(Model):
    """
    TCN + Attention Critic.
    
    Input shape: (batch, timesteps, features)
    Output shape: (batch, 1) - State value
    """
    
    def __init__(self,
                 input_dim: int,
                 tcn_filters: List[int] = None,
                 kernel_size: int = None,
                 dilations: List[int] = None,
                 attention_heads: int = None,
                 attention_dim: int = None,
                 dropout: float = None,
                 recurrent_memory_enabled: Optional[bool] = None,
                 recurrent_memory_units: Optional[int] = None,
                 recurrent_memory_dropout: Optional[float] = None,
                 regime_conditioning_enabled: Optional[bool] = None,
                 regime_conditioning_hidden_dim: Optional[int] = None,
                 regime_conditioning_dropout: Optional[float] = None,
                 regime_conditioning_mode: Optional[str] = None,
                 distributional_critic_enabled: Optional[bool] = None,
                 distributional_num_quantiles: Optional[int] = None,
                 name: str = "tcn_attention_critic"):
        super(TCNAttentionCritic, self).__init__(name=name)
        
        # Apply config defaults
        if tcn_filters is None:
            tcn_filters = _DEFAULT_TCN_FILTERS
        if kernel_size is None:
            kernel_size = _DEFAULT_TCN_KERNEL_SIZE
        if dilations is None:
            dilations = _DEFAULT_TCN_DILATIONS
        if attention_heads is None:
            attention_heads = _DEFAULT_ATTENTION_HEADS
        if attention_dim is None:
            attention_dim = _DEFAULT_ATTENTION_DIM
        if dropout is None:
            dropout = _DEFAULT_TCN_DROPOUT
        if recurrent_memory_enabled is None:
            recurrent_memory_enabled = _DEFAULT_RECURRENT_MEMORY_ENABLED
        if recurrent_memory_units is None:
            recurrent_memory_units = _DEFAULT_RECURRENT_MEMORY_UNITS
        if recurrent_memory_dropout is None:
            recurrent_memory_dropout = _DEFAULT_RECURRENT_MEMORY_DROPOUT
        if regime_conditioning_enabled is None:
            regime_conditioning_enabled = _DEFAULT_REGIME_CONDITIONING_ENABLED
        if regime_conditioning_hidden_dim is None:
            regime_conditioning_hidden_dim = _DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM
        if regime_conditioning_dropout is None:
            regime_conditioning_dropout = _DEFAULT_REGIME_CONDITIONING_DROPOUT
        if distributional_critic_enabled is None:
            distributional_critic_enabled = _DEFAULT_DISTRIBUTIONAL_CRITIC_ENABLED
        if distributional_num_quantiles is None:
            distributional_num_quantiles = _DEFAULT_DISTRIBUTIONAL_NUM_QUANTILES

        self.input_dim = input_dim
        self.recurrent_memory_enabled = bool(recurrent_memory_enabled)
        self.regime_conditioning_enabled = bool(regime_conditioning_enabled)
        self.regime_conditioning_mode = str(
            regime_conditioning_mode if regime_conditioning_mode is not None else _DEFAULT_REGIME_CONDITIONING_MODE
        ).lower().strip()
        self.distributional_critic_enabled = bool(distributional_critic_enabled)
        self.distributional_num_quantiles = max(2, int(distributional_num_quantiles))
        
        # TCN blocks
        self.tcn_blocks = []
        for i, (filters, dilation) in enumerate(zip(tcn_filters, dilations)):
            self.tcn_blocks.append(
                TCNBlock(
                    filters=filters,
                    kernel_size=kernel_size,
                    dilation_rate=dilation,
                    dropout=dropout,
                    name=f'{name}_tcn_{i}'
                )
            )
        
        # Projection
        self.projection = layers.Dense(attention_dim, name=f'{name}_projection')
        
        # Attention
        self.attention = MultiHeadSelfAttention(
            d_model=attention_dim,
            num_heads=attention_heads,
            dropout=dropout,
            name=f'{name}_attention'
        )

        self.memory_layer = None
        if self.recurrent_memory_enabled:
            self.memory_layer = layers.LSTM(
                units=max(8, int(recurrent_memory_units)),
                return_sequences=True,
                dropout=float(max(0.0, recurrent_memory_dropout)),
                name=f"{name}_memory_lstm",
            )

        # Global pooling
        self.global_pool = layers.GlobalAveragePooling1D()
        self.regime_encoder = None
        self.regime_sequence_encoder = None
        self.regime_fusion = None
        self.regime_dropout = None
        self.regime_film_layer = None
        if self.regime_conditioning_enabled:
            (
                self.regime_sequence_encoder,
                _,
                self.regime_film_layer,
                self.regime_fusion,
                self.regime_dropout,
            ) = _build_regime_conditioning_modules(
                name=name,
                feature_dim=int(attention_dim),
                hidden_dim=max(8, int(regime_conditioning_hidden_dim)),
                dropout=float(max(0.0, regime_conditioning_dropout)),
                mode=self.regime_conditioning_mode,
            )

        output_units = self.distributional_num_quantiles if self.distributional_critic_enabled else 1

        # Output layer
        self.output_layer = layers.Dense(
            output_units,
            activation=None,
            kernel_initializer='orthogonal',
            name=f'{name}_output'
        )
    
    def call(self, state, training=None):
        """
        Args:
            state: (batch, timesteps, features)
            
        Returns:
            value: (batch, 1)
        """
        x = _flatten_structured_sequence_input(state)
        
        for block in self.tcn_blocks:
            x = block(x, training=training)

        x = self.projection(x)
        x = self.attention(x, training=training)
        if self.memory_layer is not None:
            x = self.memory_layer(x, training=training)
        regime_seq = x
        x = self.global_pool(x)
        if self.regime_conditioning_enabled and self.regime_sequence_encoder is not None:
            regime_embedding = self.regime_sequence_encoder(regime_seq, training=training)
            x = _apply_regime_conditioning(
                x,
                regime_embedding,
                regime_film_layer=self.regime_film_layer,
                regime_fusion=self.regime_fusion,
                regime_dropout=self.regime_dropout,
                training=training,
            )

        value = self.output_layer(x, training=training)
        
        return value


class TCNFusionCritic(Model):
    """
    Critic counterpart of TCNFusionActor with shared fusion strategy.
    """

    def __init__(
        self,
        input_dim: int,
        tcn_filters: List[int] = None,
        kernel_size: int = None,
        dilations: List[int] = None,
        dropout: float = None,
        num_assets: int = None,
        asset_feature_dim: int = None,
        global_feature_dim: int = None,
        fusion_embed_dim: int = None,
        fusion_attention_heads: int = None,
        fusion_dropout: float = None,
        fusion_cross_asset_mixer_enabled: Optional[bool] = None,
        fusion_cross_asset_mixer_layers: Optional[int] = None,
        fusion_cross_asset_mixer_expansion: Optional[float] = None,
        fusion_cross_asset_mixer_dropout: Optional[float] = None,
        fusion_asset_identity_enabled: Optional[bool] = None,
        fusion_context_cross_attention_enabled: Optional[bool] = None,
        fusion_context_cross_attention_heads: Optional[int] = None,
        fusion_context_cross_attention_dropout: Optional[float] = None,
        recurrent_memory_enabled: Optional[bool] = None,
        recurrent_memory_units: Optional[int] = None,
        recurrent_memory_dropout: Optional[float] = None,
        regime_conditioning_enabled: Optional[bool] = None,
        regime_conditioning_hidden_dim: Optional[int] = None,
        regime_conditioning_dropout: Optional[float] = None,
        regime_conditioning_mode: Optional[str] = None,
        distributional_critic_enabled: Optional[bool] = None,
        distributional_num_quantiles: Optional[int] = None,
        name: str = "tcn_fusion_critic",
    ):
        super(TCNFusionCritic, self).__init__(name=name)

        if tcn_filters is None:
            tcn_filters = _DEFAULT_TCN_FILTERS
        if kernel_size is None:
            kernel_size = _DEFAULT_TCN_KERNEL_SIZE
        if dilations is None:
            dilations = _DEFAULT_TCN_DILATIONS
        if dropout is None:
            dropout = _DEFAULT_TCN_DROPOUT
        if fusion_embed_dim is None:
            fusion_embed_dim = _DEFAULT_FUSION_EMBED_DIM
        if fusion_attention_heads is None:
            fusion_attention_heads = _DEFAULT_FUSION_HEADS
        if fusion_dropout is None:
            fusion_dropout = _DEFAULT_FUSION_DROPOUT
        if fusion_cross_asset_mixer_enabled is None:
            fusion_cross_asset_mixer_enabled = _DEFAULT_FUSION_CROSS_ASSET_MIXER_ENABLED
        if fusion_cross_asset_mixer_layers is None:
            fusion_cross_asset_mixer_layers = _DEFAULT_FUSION_CROSS_ASSET_MIXER_LAYERS
        if fusion_cross_asset_mixer_expansion is None:
            fusion_cross_asset_mixer_expansion = _DEFAULT_FUSION_CROSS_ASSET_MIXER_EXPANSION
        if fusion_cross_asset_mixer_dropout is None:
            fusion_cross_asset_mixer_dropout = _DEFAULT_FUSION_CROSS_ASSET_MIXER_DROPOUT
        if fusion_asset_identity_enabled is None:
            fusion_asset_identity_enabled = _DEFAULT_FUSION_ASSET_IDENTITY_ENABLED
        if fusion_context_cross_attention_enabled is None:
            fusion_context_cross_attention_enabled = _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_ENABLED
        if fusion_context_cross_attention_heads is None:
            fusion_context_cross_attention_heads = _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_HEADS
        if fusion_context_cross_attention_dropout is None:
            fusion_context_cross_attention_dropout = _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_DROPOUT
        if recurrent_memory_enabled is None:
            recurrent_memory_enabled = _DEFAULT_RECURRENT_MEMORY_ENABLED
        if recurrent_memory_units is None:
            recurrent_memory_units = _DEFAULT_RECURRENT_MEMORY_UNITS
        if recurrent_memory_dropout is None:
            recurrent_memory_dropout = _DEFAULT_RECURRENT_MEMORY_DROPOUT
        if regime_conditioning_enabled is None:
            regime_conditioning_enabled = _DEFAULT_REGIME_CONDITIONING_ENABLED
        if regime_conditioning_hidden_dim is None:
            regime_conditioning_hidden_dim = _DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM
        if regime_conditioning_dropout is None:
            regime_conditioning_dropout = _DEFAULT_REGIME_CONDITIONING_DROPOUT
        if distributional_critic_enabled is None:
            distributional_critic_enabled = _DEFAULT_DISTRIBUTIONAL_CRITIC_ENABLED
        if distributional_num_quantiles is None:
            distributional_num_quantiles = _DEFAULT_DISTRIBUTIONAL_NUM_QUANTILES

        self.input_dim = int(input_dim)
        self.num_assets = int(num_assets) if num_assets is not None else 5
        if asset_feature_dim is not None and int(asset_feature_dim) > 0:
            self.per_asset_dim = int(asset_feature_dim)
        else:
            self.per_asset_dim = int(np.ceil(self.input_dim / max(1, self.num_assets)))
        self.local_flat_dim = self.per_asset_dim * self.num_assets
        if global_feature_dim is not None:
            self.global_feature_dim = max(0, int(global_feature_dim))
        else:
            self.global_feature_dim = max(0, int(self.input_dim) - self.local_flat_dim)
        self.expected_input_dim = self.local_flat_dim + self.global_feature_dim
        self.fusion_embed_dim = int(fusion_embed_dim)
        self.recurrent_memory_enabled = bool(recurrent_memory_enabled)
        self.regime_conditioning_enabled = bool(regime_conditioning_enabled)
        self.distributional_critic_enabled = bool(distributional_critic_enabled)
        self.distributional_num_quantiles = max(2, int(distributional_num_quantiles))

        if self.fusion_embed_dim % fusion_attention_heads != 0:
            fusion_attention_heads = 1
        self.fusion_attention_heads = int(fusion_attention_heads)

        self.asset_tcn_blocks = []
        for i, (filters, dilation) in enumerate(zip(tcn_filters, dilations)):
            self.asset_tcn_blocks.append(
                TCNBlock(
                    filters=filters,
                    kernel_size=kernel_size,
                    dilation_rate=dilation,
                    dropout=dropout,
                    name=f"{name}_asset_tcn_{i}",
                )
            )
        self.asset_memory_layer = None
        self.global_memory_layer = None
        if self.recurrent_memory_enabled:
            mem_units = max(8, int(recurrent_memory_units))
            mem_dropout = float(max(0.0, recurrent_memory_dropout))
            self.asset_memory_layer = layers.LSTM(
                units=mem_units,
                return_sequences=True,
                dropout=mem_dropout,
                name=f"{name}_asset_memory_lstm",
            )
            self.global_memory_layer = layers.LSTM(
                units=mem_units,
                return_sequences=True,
                dropout=mem_dropout,
                name=f"{name}_global_memory_lstm",
            )

        self.asset_time_pool = layers.GlobalAveragePooling1D()
        self.asset_projection = layers.Dense(self.fusion_embed_dim, activation="relu", name=f"{name}_asset_projection")
        self.asset_attention = MultiHeadSelfAttention(
            d_model=self.fusion_embed_dim,
            num_heads=self.fusion_attention_heads,
            dropout=fusion_dropout,
            name=f"{name}_asset_attention",
        )
        self.asset_mixer_blocks: List[CrossAssetMixerBlock] = []
        self.cross_asset_mixer_enabled = bool(fusion_cross_asset_mixer_enabled)
        if self.cross_asset_mixer_enabled:
            mixer_layers = max(1, int(fusion_cross_asset_mixer_layers))
            mixer_dropout = float(fusion_cross_asset_mixer_dropout)
            mixer_expansion = float(fusion_cross_asset_mixer_expansion)
            for i in range(mixer_layers):
                self.asset_mixer_blocks.append(
                    CrossAssetMixerBlock(
                        d_model=self.fusion_embed_dim,
                        num_heads=self.fusion_attention_heads,
                        expansion=mixer_expansion,
                        dropout=mixer_dropout,
                        name=f"{name}_asset_mixer_{i}",
                    )
                )
        # --- Cross-Asset Attention v2 upgrades (critic) ---

        # Change 1: Learnable asset identity embeddings
        self.asset_identity_enabled = bool(fusion_asset_identity_enabled)
        self.asset_identity_embed = None
        if self.asset_identity_enabled:
            self.asset_identity_embed = self.add_weight(
                name=f"{name}_asset_identity",
                shape=(self.num_assets, self.fusion_embed_dim),
                initializer=tf.keras.initializers.TruncatedNormal(stddev=0.02),
                trainable=True,
            )

        # Change 2: Context cross-attention
        self.context_cross_attn_enabled = bool(fusion_context_cross_attention_enabled)
        self.context_cross_attn_block = None
        self.context_projection_critic = None
        if self.context_cross_attn_enabled:
            ctx_heads = int(fusion_context_cross_attention_heads)
            ctx_dropout = float(fusion_context_cross_attention_dropout)
            self.context_cross_attn_block = ContextCrossAttentionBlock(
                d_model=self.fusion_embed_dim,
                num_heads=ctx_heads,
                expansion=2.0,
                dropout=ctx_dropout,
                name=f"{name}_ctx_cross_attn",
            )
            self.context_projection_critic = layers.Dense(
                self.fusion_embed_dim, activation="relu",
                name=f"{name}_ctx_projection",
            )
        # 3-layer stack mode:
        # self-attn (mixer[0]) -> context cross-attn -> self-attn (mixer[1:]).
        self.use_three_layer_context_stack = bool(
            self.context_cross_attn_enabled
            and self.cross_asset_mixer_enabled
            and len(self.asset_mixer_blocks) >= 2
        )

        # Critic always pools to scalar — but enriched per-asset representations help
        self.asset_pool = layers.GlobalAveragePooling1D()

        self.global_time_pool = layers.GlobalAveragePooling1D()
        self.global_projection = layers.Dense(self.fusion_embed_dim, activation="relu", name=f"{name}_global_projection")
        self.global_dropout = layers.Dropout(fusion_dropout)
        self.gate_layer = layers.Dense(self.fusion_embed_dim, activation="sigmoid", name=f"{name}_gate")
        self.regime_encoder = None
        self.regime_sequence_encoder = None
        self.regime_sequence_film_layer = None
        self.regime_context_sequence_film_layer = None
        self.regime_fusion = None
        self.regime_dropout = None
        self.regime_film_layer = None
        self.regime_conditioning_mode = 'concat'
        if self.regime_conditioning_enabled:
            rc_mode = str(regime_conditioning_mode) if regime_conditioning_mode else _DEFAULT_REGIME_CONDITIONING_MODE
            self.regime_conditioning_mode = str(rc_mode).lower().strip()
            (
                self.regime_sequence_encoder,
                self.regime_sequence_film_layer,
                self.regime_film_layer,
                self.regime_fusion,
                self.regime_dropout,
            ) = _build_regime_conditioning_modules(
                name=name,
                feature_dim=self.fusion_embed_dim,
                hidden_dim=max(8, int(regime_conditioning_hidden_dim)),
                dropout=float(max(0.0, regime_conditioning_dropout)),
                mode=self.regime_conditioning_mode,
                sequence_film_feature_dim=self.per_asset_dim,
                latent_gamma_limit=0.25,
                latent_beta_limit=0.15,
                sequence_gamma_limit=0.12,
                sequence_beta_limit=0.08,
            )
            if self.regime_conditioning_mode == "film" and self.global_feature_dim > 0:
                self.regime_context_sequence_film_layer = FiLMLayer(
                    feature_dim=self.global_feature_dim,
                    conditioning_dim=max(8, int(regime_conditioning_hidden_dim)),
                    hidden_dim=max(8, int(regime_conditioning_hidden_dim // 2) or 8),
                    dropout=0.0,
                    gamma_limit=0.12,
                    beta_limit=0.08,
                    name=f"{name}_regime_context_sequence_film",
                )

        output_units = self.distributional_num_quantiles if self.distributional_critic_enabled else 1
        self.output_layer = layers.Dense(output_units, activation=None, kernel_initializer="orthogonal", name=f"{name}_output")

    def _align_feature_dim(self, x: tf.Tensor) -> tf.Tensor:
        current_dim = tf.shape(x)[-1]
        pad_dim = tf.maximum(0, self.expected_input_dim - current_dim)
        x = tf.pad(x, [[0, 0], [0, 0], [0, pad_dim]])
        return x[:, :, : self.expected_input_dim]

    def _align_asset_tensor(self, asset_tensor: tf.Tensor) -> tf.Tensor:
        x_assets = _to_tensor_with_cast(asset_tensor, tf.float32)
        if x_assets.shape.rank != 4:
            raise ValueError(
                f"TCNFusionCritic expects asset tensor rank=4 (batch,time,assets,features), got shape {x_assets.shape}"
            )
        pad_assets = tf.maximum(0, self.num_assets - tf.shape(x_assets)[2])
        x_assets = tf.pad(x_assets, [[0, 0], [0, 0], [0, pad_assets], [0, 0]])
        x_assets = x_assets[:, :, : self.num_assets, :]

        pad_feat = tf.maximum(0, self.per_asset_dim - tf.shape(x_assets)[-1])
        x_assets = tf.pad(x_assets, [[0, 0], [0, 0], [0, 0], [0, pad_feat]])
        x_assets = x_assets[:, :, :, : self.per_asset_dim]
        return x_assets

    def _align_context_tensor(
        self,
        context_tensor: tf.Tensor,
        *,
        batch: tf.Tensor,
        timesteps: tf.Tensor,
        fallback: tf.Tensor,
    ) -> tf.Tensor:
        target_dim = int(self.global_feature_dim)
        if target_dim <= 0:
            return fallback

        if context_tensor is None:
            return tf.zeros((batch, timesteps, target_dim), dtype=fallback.dtype)

        context = _to_tensor_with_cast(context_tensor, fallback.dtype)
        if context.shape.rank == 2:
            context = tf.expand_dims(context, axis=1)
        elif context.shape.rank != 3:
            raise ValueError(
                f"TCNFusionCritic expects context rank=2 or 3, got shape {context.shape}"
            )

        pad_time = tf.maximum(0, timesteps - tf.shape(context)[1])
        context = tf.pad(context, [[0, 0], [0, pad_time], [0, 0]])
        context = context[:, :timesteps, :]

        pad_dim = tf.maximum(0, target_dim - tf.shape(context)[-1])
        context = tf.pad(context, [[0, 0], [0, 0], [0, pad_dim]])
        context = context[:, :, :target_dim]
        return context

    def call(self, state, training=None):
        if isinstance(state, dict):
            structured_assets = self._align_asset_tensor(state.get("asset"))
            batch = tf.shape(structured_assets)[0]
            timesteps = tf.shape(structured_assets)[1]
            x_assets = tf.transpose(structured_assets, perm=[0, 2, 1, 3])
            x_assets = tf.reshape(x_assets, (-1, timesteps, self.per_asset_dim))

            context_seq = self._align_context_tensor(
                state.get("context"),
                batch=batch,
                timesteps=timesteps,
                fallback=tf.zeros((batch, timesteps, self.per_asset_dim), dtype=structured_assets.dtype),
            )
            asset_flat_for_regime = tf.reshape(
                structured_assets,
                (batch, timesteps, self.num_assets * self.per_asset_dim),
            )
            regime_seq = tf.concat([asset_flat_for_regime, context_seq], axis=-1)
        else:
            x = self._align_feature_dim(state)
            batch = tf.shape(x)[0]
            timesteps = tf.shape(x)[1]
            x_local = x[:, :, : self.local_flat_dim]

            x_assets = tf.reshape(x_local, (batch, timesteps, self.num_assets, self.per_asset_dim))
            x_assets = tf.transpose(x_assets, perm=[0, 2, 1, 3])
            x_assets = tf.reshape(x_assets, (-1, timesteps, self.per_asset_dim))

            x_context = x[:, :, self.local_flat_dim:]
            if self.global_feature_dim <= 0:
                context_seq = x_local
            else:
                context_seq = self._align_context_tensor(
                    x_context,
                    batch=batch,
                    timesteps=timesteps,
                    fallback=x_local,
                )
            regime_seq = x

        regime_embedding = None
        if self.regime_conditioning_enabled and self.regime_sequence_encoder is not None:
            regime_embedding = self.regime_sequence_encoder(regime_seq, training=training)
        if regime_embedding is not None and self.regime_sequence_film_layer is not None:
            asset_regime_embedding = tf.repeat(regime_embedding, repeats=self.num_assets, axis=0)
            x_assets = self.regime_sequence_film_layer(x_assets, asset_regime_embedding, training=training)
        if regime_embedding is not None and self.regime_context_sequence_film_layer is not None:
            context_seq = self.regime_context_sequence_film_layer(context_seq, regime_embedding, training=training)

        # --- Per-asset TCN encoding (shared weights) ---
        for block in self.asset_tcn_blocks:
            x_assets = block(x_assets, training=training)
        if self.asset_memory_layer is not None:
            x_assets = self.asset_memory_layer(x_assets, training=training)

        x_assets = self.asset_time_pool(x_assets)
        x_assets = self.asset_projection(x_assets)
        x_assets = tf.reshape(x_assets, (batch, self.num_assets, self.fusion_embed_dim))

        # --- Change 1: Asset identity embeddings ---
        if self.asset_identity_embed is not None:
            x_assets = x_assets + self.asset_identity_embed[tf.newaxis, :, :]

        # --- Cross-asset attention stack ---
        if self.use_three_layer_context_stack:
            x_assets = self.asset_mixer_blocks[0](x_assets, training=training)
        else:
            x_assets = self.asset_attention(x_assets, training=training)
            for mixer_block in self.asset_mixer_blocks:
                x_assets = mixer_block(x_assets, training=training)

        # --- Global context branch ---
        if self.global_memory_layer is not None:
            context_seq = self.global_memory_layer(context_seq, training=training)
        global_context = self.global_time_pool(context_seq)
        global_context = self.global_projection(global_context)
        global_context = self.global_dropout(global_context, training=training)

        # --- Change 2: Context cross-attention OR legacy gate ---
        if self.context_cross_attn_enabled and self.context_cross_attn_block is not None:
            ctx_token = self.context_projection_critic(global_context)  # (batch, embed_dim)
            ctx_token = tf.expand_dims(ctx_token, axis=1)  # (batch, 1, embed_dim)
            x_assets = self.context_cross_attn_block(
                query=x_assets, context=ctx_token, training=training,
            )
            if self.use_three_layer_context_stack:
                for mixer_block in self.asset_mixer_blocks[1:]:
                    x_assets = mixer_block(x_assets, training=training)
            # Pool enriched asset representations for critic value
            fused = self.asset_pool(x_assets)
        else:
            asset_context = self.asset_pool(x_assets)
            gate = self.gate_layer(tf.concat([asset_context, global_context], axis=-1))
            fused = gate * asset_context + (1.0 - gate) * global_context

        # --- Regime conditioning ---
        if regime_embedding is not None:
            fused = _apply_regime_conditioning(
                fused,
                regime_embedding,
                regime_film_layer=self.regime_film_layer,
                regime_fusion=self.regime_fusion,
                regime_dropout=self.regime_dropout,
                training=training,
            )

        return self.output_layer(fused, training=training)


# ============================================================================
# ARCHITECTURE FACTORY
# ============================================================================

def _resolve_dirichlet_epsilon_kwargs(config: Dict[str, Any]) -> Dict[str, Any]:
    """Extract Dirichlet-related defaults from config."""
    epsilon_cfg = config.get("dirichlet_epsilon") or {}
    epsilon_start = float(epsilon_cfg.get("max", epsilon_cfg.get("start", 0.5)))
    epsilon_min = float(epsilon_cfg.get("min", 0.1))
    alpha_activation = str(config.get("dirichlet_alpha_activation", _DEFAULT_ALPHA_ACTIVATION))
    exp_clip_cfg = config.get("dirichlet_exp_clip", (-5.0, 3.0))
    try:
        exp_clip = (float(exp_clip_cfg[0]), float(exp_clip_cfg[1]))
    except Exception:
        exp_clip = (-5.0, 3.0)
    return {
        "epsilon_start": epsilon_start,
        "epsilon_min": epsilon_min,
        "alpha_activation": alpha_activation,
        "exp_clip": exp_clip,
        "exp_tanh_scale": float(config.get("dirichlet_exp_tanh_scale", 2.5)),
        "softplus_alpha_floor": float(config.get("dirichlet_softplus_alpha_floor", 0.0)),
        "softplus_alpha_scale": float(config.get("dirichlet_softplus_alpha_scale", 1.0)),
        "cross_sectional_standardize": bool(config.get("dirichlet_cross_sectional_standardize", False)),
        # New parameters
        "logit_temperature": float(config.get("dirichlet_logit_temperature", 1.0)),
        "alpha_cap": float(config.get("dirichlet_alpha_cap", 100.0)) if "dirichlet_alpha_cap" in config else None,
        # Optional adaptive temperature controller (disabled by default).
        "adaptive_temperature_enabled": bool(config.get("dirichlet_adaptive_temperature_enabled", False)),
        "adaptive_temperature_base": float(
            config.get("dirichlet_adaptive_temperature_base", config.get("dirichlet_logit_temperature", 1.0))
        ),
        "adaptive_temperature_slope": float(config.get("dirichlet_adaptive_temperature_slope", 0.0)),
        "adaptive_temperature_min": float(config.get("dirichlet_adaptive_temperature_min", 0.8)),
        "adaptive_temperature_max": float(config.get("dirichlet_adaptive_temperature_max", 2.5)),
    }


def create_actor_critic(architecture: str,
                       input_dim: int,
                       num_actions: int,
                       config: dict) -> Tuple[Model, Model]:
    """
    Factory function to create Actor and Critic networks based on architecture type.
    
    Args:
        architecture: One of ['MLP', 'TCN', 'TCN_ATTENTION', 'TCN_FUSION']
        input_dim: Input dimension for sequential models
        num_actions: Number of actions (assets + cash)
        config: Configuration dictionary with architecture-specific parameters
        
    Returns:
        Tuple of (actor_network, critic_network)
    """
    arch_upper = architecture.upper()
    global _RUNTIME_STATE_AUGMENTATION_ENABLED
    _RUNTIME_STATE_AUGMENTATION_ENABLED = bool(
        config.get("state_augmentation_enabled", _DEFAULT_STATE_AUGMENTATION_ENABLED)
    )
    epsilon_kwargs = _resolve_dirichlet_epsilon_kwargs(config)
    state_layout = config.get("state_layout", {}) if isinstance(config.get("state_layout", {}), dict) else {}
    resolved_asset_feature_dim = state_layout.get("asset_feature_dim", config.get("asset_feature_dim"))
    resolved_global_feature_dim = state_layout.get("global_feature_dim", config.get("global_feature_dim"))
    recurrent_kwargs = {
        "recurrent_memory_enabled": bool(config.get("recurrent_memory_enabled", _DEFAULT_RECURRENT_MEMORY_ENABLED)),
        "recurrent_memory_units": int(config.get("recurrent_memory_units", _DEFAULT_RECURRENT_MEMORY_UNITS)),
        "recurrent_memory_dropout": float(config.get("recurrent_memory_dropout", _DEFAULT_RECURRENT_MEMORY_DROPOUT)),
    }
    regime_kwargs = {
        "regime_conditioning_enabled": bool(
            config.get("regime_conditioning_enabled", _DEFAULT_REGIME_CONDITIONING_ENABLED)
        ),
        "regime_conditioning_hidden_dim": int(
            config.get("regime_conditioning_hidden_dim", _DEFAULT_REGIME_CONDITIONING_HIDDEN_DIM)
        ),
        "regime_conditioning_dropout": float(
            config.get("regime_conditioning_dropout", _DEFAULT_REGIME_CONDITIONING_DROPOUT)
        ),
        "regime_conditioning_mode": str(
            config.get("regime_conditioning_mode", _DEFAULT_REGIME_CONDITIONING_MODE)
        ),
    }
    critic_distributional_kwargs = {
        "distributional_critic_enabled": bool(
            config.get("distributional_critic_enabled", _DEFAULT_DISTRIBUTIONAL_CRITIC_ENABLED)
        ),
        "distributional_num_quantiles": int(
            config.get("distributional_num_quantiles", _DEFAULT_DISTRIBUTIONAL_NUM_QUANTILES)
        ),
    }
    dual_head_enabled_cfg = bool(config.get("dual_head_enabled", _DEFAULT_DUAL_HEAD_ENABLED))
    mixture_kwargs = {
        "mixture_dirichlet_enabled": bool(
            config.get("mixture_dirichlet_enabled", _DEFAULT_MIXTURE_DIRICHLET_ENABLED)
        ),
        "mixture_dirichlet_num_components": int(
            config.get("mixture_dirichlet_num_components", _DEFAULT_MIXTURE_DIRICHLET_COMPONENTS)
        ),
        "mixture_dirichlet_gating_hidden_dims": list(
            config.get("mixture_dirichlet_gating_hidden_dims", _DEFAULT_MIXTURE_DIRICHLET_GATING_HIDDEN_DIMS)
        ),
        "mixture_dirichlet_component_hidden_dims": list(
            config.get("mixture_dirichlet_component_hidden_dims", _DEFAULT_MIXTURE_DIRICHLET_COMPONENT_HIDDEN_DIMS)
        ),
    }
    ppo_params_cfg = config.get("ppo_params", {}) if isinstance(config.get("ppo_params", {}), dict) else {}
    aux_return_enabled_cfg = bool(
        config.get("aux_return_pred_enabled", ppo_params_cfg.get("aux_return_pred_enabled", False))
    )
    if arch_upper == 'MLP':
        actor = MLPActor(
            input_dim=input_dim,
            num_actions=num_actions,
            sequence_length=int(config.get('sequence_length', 60)),
            hidden_dims=config.get('actor_hidden_dims', _DEFAULT_ACTOR_HIDDEN_DIMS),
            dropout=config.get('mlp_dropout', config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT)),
            dual_head_enabled=dual_head_enabled_cfg,
            **mixture_kwargs,
            aux_return_enabled=aux_return_enabled_cfg,
            **regime_kwargs,
            **epsilon_kwargs,
        )
        critic = MLPCritic(
            input_dim=input_dim,
            sequence_length=int(config.get('sequence_length', 60)),
            hidden_dims=config.get('critic_hidden_dims', _DEFAULT_CRITIC_HIDDEN_DIMS),
            dropout=config.get('mlp_dropout', config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT)),
            **regime_kwargs,
            **critic_distributional_kwargs,
        )

    elif arch_upper == 'TCN':
        if config.get('use_fusion', False):
            resolved_num_assets = int(config.get('num_assets', max(1, num_actions - 1)))
            actor = TCNFusionActor(
                input_dim=input_dim,
                num_actions=num_actions,
                tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
                kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
                dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
                dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
                num_assets=resolved_num_assets,
                asset_feature_dim=resolved_asset_feature_dim,
                global_feature_dim=resolved_global_feature_dim,
                fusion_embed_dim=config.get('fusion_embed_dim', _DEFAULT_FUSION_EMBED_DIM),
                fusion_attention_heads=config.get('fusion_attention_heads', _DEFAULT_FUSION_HEADS),
                fusion_dropout=config.get('fusion_dropout', _DEFAULT_FUSION_DROPOUT),
                fusion_cross_asset_mixer_enabled=config.get('fusion_cross_asset_mixer_enabled', _DEFAULT_FUSION_CROSS_ASSET_MIXER_ENABLED),
                fusion_cross_asset_mixer_layers=config.get('fusion_cross_asset_mixer_layers', _DEFAULT_FUSION_CROSS_ASSET_MIXER_LAYERS),
                fusion_cross_asset_mixer_expansion=config.get('fusion_cross_asset_mixer_expansion', _DEFAULT_FUSION_CROSS_ASSET_MIXER_EXPANSION),
                fusion_cross_asset_mixer_dropout=config.get('fusion_cross_asset_mixer_dropout', _DEFAULT_FUSION_CROSS_ASSET_MIXER_DROPOUT),
                fusion_alpha_head_hidden_dims=config.get('fusion_alpha_head_hidden_dims', _DEFAULT_FUSION_ALPHA_HEAD_HIDDEN_DIMS),
                fusion_alpha_head_dropout=config.get('fusion_alpha_head_dropout', _DEFAULT_FUSION_ALPHA_HEAD_DROPOUT),
                fusion_asset_identity_enabled=config.get('fusion_asset_identity_enabled', _DEFAULT_FUSION_ASSET_IDENTITY_ENABLED),
                fusion_context_cross_attention_enabled=config.get('fusion_context_cross_attention_enabled', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_ENABLED),
                fusion_context_cross_attention_heads=config.get('fusion_context_cross_attention_heads', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_HEADS),
                fusion_context_cross_attention_dropout=config.get('fusion_context_cross_attention_dropout', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_DROPOUT),
                fusion_per_asset_alpha_head=config.get('fusion_per_asset_alpha_head', _DEFAULT_FUSION_PER_ASSET_ALPHA_HEAD),
                dual_head_enabled=dual_head_enabled_cfg,
                **mixture_kwargs,
                aux_return_enabled=aux_return_enabled_cfg,
                **recurrent_kwargs,
                **regime_kwargs,
                **epsilon_kwargs,
            )
            critic = TCNFusionCritic(
                input_dim=input_dim,
                tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
                kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
                dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
                dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
                num_assets=resolved_num_assets,
                asset_feature_dim=resolved_asset_feature_dim,
                global_feature_dim=resolved_global_feature_dim,
                fusion_embed_dim=config.get('fusion_embed_dim', _DEFAULT_FUSION_EMBED_DIM),
                fusion_attention_heads=config.get('fusion_attention_heads', _DEFAULT_FUSION_HEADS),
                fusion_dropout=config.get('fusion_dropout', _DEFAULT_FUSION_DROPOUT),
                fusion_cross_asset_mixer_enabled=config.get('fusion_cross_asset_mixer_enabled', _DEFAULT_FUSION_CROSS_ASSET_MIXER_ENABLED),
                fusion_cross_asset_mixer_layers=config.get('fusion_cross_asset_mixer_layers', _DEFAULT_FUSION_CROSS_ASSET_MIXER_LAYERS),
                fusion_cross_asset_mixer_expansion=config.get('fusion_cross_asset_mixer_expansion', _DEFAULT_FUSION_CROSS_ASSET_MIXER_EXPANSION),
                fusion_cross_asset_mixer_dropout=config.get('fusion_cross_asset_mixer_dropout', _DEFAULT_FUSION_CROSS_ASSET_MIXER_DROPOUT),
                fusion_asset_identity_enabled=config.get('fusion_asset_identity_enabled', _DEFAULT_FUSION_ASSET_IDENTITY_ENABLED),
                fusion_context_cross_attention_enabled=config.get('fusion_context_cross_attention_enabled', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_ENABLED),
                fusion_context_cross_attention_heads=config.get('fusion_context_cross_attention_heads', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_HEADS),
                fusion_context_cross_attention_dropout=config.get('fusion_context_cross_attention_dropout', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_DROPOUT),
                **recurrent_kwargs,
                **regime_kwargs,
                **critic_distributional_kwargs,
            )
        elif config.get('use_attention', False):
            actor = TCNAttentionActor(
                input_dim=input_dim,
                num_actions=num_actions,
                tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
                kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
                dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
                attention_heads=config.get('attention_heads', _DEFAULT_ATTENTION_HEADS),
                attention_dim=config.get('attention_dim', _DEFAULT_ATTENTION_DIM),
                dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
                dual_head_enabled=dual_head_enabled_cfg,
                **recurrent_kwargs,
                **regime_kwargs,
                **epsilon_kwargs,
            )
            critic = TCNAttentionCritic(
                input_dim=input_dim,
                tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
                kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
                dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
                attention_heads=config.get('attention_heads', _DEFAULT_ATTENTION_HEADS),
                attention_dim=config.get('attention_dim', _DEFAULT_ATTENTION_DIM),
                dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
                **recurrent_kwargs,
                **regime_kwargs,
                **critic_distributional_kwargs,
            )
        else:
            actor = TCNActor(
                input_dim=input_dim,
                num_actions=num_actions,
                tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
                kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
                dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
                dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
                dual_head_enabled=dual_head_enabled_cfg,
                **recurrent_kwargs,
                **regime_kwargs,
                **epsilon_kwargs,
            )
            critic = TCNCritic(
                input_dim=input_dim,
                tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
                kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
                dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
                dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
                **recurrent_kwargs,
                **regime_kwargs,
                **critic_distributional_kwargs,
            )

    elif arch_upper == 'TCN_FUSION':
        resolved_num_assets = int(config.get('num_assets', max(1, num_actions - 1)))
        actor = TCNFusionActor(
            input_dim=input_dim,
            num_actions=num_actions,
            tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
            kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
            dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
            dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
            num_assets=resolved_num_assets,
            asset_feature_dim=resolved_asset_feature_dim,
            global_feature_dim=resolved_global_feature_dim,
            fusion_embed_dim=config.get('fusion_embed_dim', _DEFAULT_FUSION_EMBED_DIM),
            fusion_attention_heads=config.get('fusion_attention_heads', _DEFAULT_FUSION_HEADS),
            fusion_dropout=config.get('fusion_dropout', _DEFAULT_FUSION_DROPOUT),
            fusion_cross_asset_mixer_enabled=config.get('fusion_cross_asset_mixer_enabled', _DEFAULT_FUSION_CROSS_ASSET_MIXER_ENABLED),
            fusion_cross_asset_mixer_layers=config.get('fusion_cross_asset_mixer_layers', _DEFAULT_FUSION_CROSS_ASSET_MIXER_LAYERS),
            fusion_cross_asset_mixer_expansion=config.get('fusion_cross_asset_mixer_expansion', _DEFAULT_FUSION_CROSS_ASSET_MIXER_EXPANSION),
            fusion_cross_asset_mixer_dropout=config.get('fusion_cross_asset_mixer_dropout', _DEFAULT_FUSION_CROSS_ASSET_MIXER_DROPOUT),
            fusion_alpha_head_hidden_dims=config.get('fusion_alpha_head_hidden_dims', _DEFAULT_FUSION_ALPHA_HEAD_HIDDEN_DIMS),
            fusion_alpha_head_dropout=config.get('fusion_alpha_head_dropout', _DEFAULT_FUSION_ALPHA_HEAD_DROPOUT),
            fusion_asset_identity_enabled=config.get('fusion_asset_identity_enabled', _DEFAULT_FUSION_ASSET_IDENTITY_ENABLED),
            fusion_context_cross_attention_enabled=config.get('fusion_context_cross_attention_enabled', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_ENABLED),
            fusion_context_cross_attention_heads=config.get('fusion_context_cross_attention_heads', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_HEADS),
            fusion_context_cross_attention_dropout=config.get('fusion_context_cross_attention_dropout', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_DROPOUT),
            fusion_per_asset_alpha_head=config.get('fusion_per_asset_alpha_head', _DEFAULT_FUSION_PER_ASSET_ALPHA_HEAD),
            dual_head_enabled=dual_head_enabled_cfg,
            **mixture_kwargs,
            aux_return_enabled=aux_return_enabled_cfg,
            exp_tanh_scale=float(config.get('dirichlet_exp_tanh_scale', 2.5)),
            **recurrent_kwargs,
            **regime_kwargs,
            **epsilon_kwargs,
        )
        critic = TCNFusionCritic(
            input_dim=input_dim,
            tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
            kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
            dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
            dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
            num_assets=resolved_num_assets,
            asset_feature_dim=resolved_asset_feature_dim,
            global_feature_dim=resolved_global_feature_dim,
            fusion_embed_dim=config.get('fusion_embed_dim', _DEFAULT_FUSION_EMBED_DIM),
            fusion_attention_heads=config.get('fusion_attention_heads', _DEFAULT_FUSION_HEADS),
            fusion_dropout=config.get('fusion_dropout', _DEFAULT_FUSION_DROPOUT),
            fusion_cross_asset_mixer_enabled=config.get('fusion_cross_asset_mixer_enabled', _DEFAULT_FUSION_CROSS_ASSET_MIXER_ENABLED),
            fusion_cross_asset_mixer_layers=config.get('fusion_cross_asset_mixer_layers', _DEFAULT_FUSION_CROSS_ASSET_MIXER_LAYERS),
            fusion_cross_asset_mixer_expansion=config.get('fusion_cross_asset_mixer_expansion', _DEFAULT_FUSION_CROSS_ASSET_MIXER_EXPANSION),
            fusion_cross_asset_mixer_dropout=config.get('fusion_cross_asset_mixer_dropout', _DEFAULT_FUSION_CROSS_ASSET_MIXER_DROPOUT),
            fusion_asset_identity_enabled=config.get('fusion_asset_identity_enabled', _DEFAULT_FUSION_ASSET_IDENTITY_ENABLED),
            fusion_context_cross_attention_enabled=config.get('fusion_context_cross_attention_enabled', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_ENABLED),
            fusion_context_cross_attention_heads=config.get('fusion_context_cross_attention_heads', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_HEADS),
            fusion_context_cross_attention_dropout=config.get('fusion_context_cross_attention_dropout', _DEFAULT_FUSION_CONTEXT_CROSS_ATTN_DROPOUT),
            **recurrent_kwargs,
            **regime_kwargs,
            **critic_distributional_kwargs,
        )

    elif arch_upper == 'TCN_ATTENTION':
        actor = TCNAttentionActor(
            input_dim=input_dim,
            num_actions=num_actions,
            tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
            kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
            dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
            attention_heads=config.get('attention_heads', _DEFAULT_ATTENTION_HEADS),
            attention_dim=config.get('attention_dim', _DEFAULT_ATTENTION_DIM),
            dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
            dual_head_enabled=dual_head_enabled_cfg,
            **recurrent_kwargs,
            **regime_kwargs,
            **epsilon_kwargs,
        )
        critic = TCNAttentionCritic(
            input_dim=input_dim,
            tcn_filters=config.get('tcn_filters', _DEFAULT_TCN_FILTERS),
            kernel_size=config.get('tcn_kernel_size', _DEFAULT_TCN_KERNEL_SIZE),
            dilations=config.get('tcn_dilations', _DEFAULT_TCN_DILATIONS),
            attention_heads=config.get('attention_heads', _DEFAULT_ATTENTION_HEADS),
            attention_dim=config.get('attention_dim', _DEFAULT_ATTENTION_DIM),
            dropout=config.get('tcn_dropout', _DEFAULT_TCN_DROPOUT),
            **recurrent_kwargs,
            **regime_kwargs,
            **critic_distributional_kwargs,
        )
    
    else:
        raise ValueError(
            f"Unknown architecture: {architecture}. "
            f"Must be one of: MLP, TCN, TCN_ATTENTION, TCN_FUSION"
        )
    
    return actor, critic
