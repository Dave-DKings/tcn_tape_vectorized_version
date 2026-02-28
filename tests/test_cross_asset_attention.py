#!/usr/bin/env python3
"""
Verification test for Cross-Asset Attention v2 architecture upgrades.

Tests:
1. TCNFusionActor builds with all 3 features enabled
2. TCNFusionCritic builds with all 3 features enabled
3. Forward pass with structured dict input
4. Forward pass with flat tensor input (backward compat)
5. Output shapes are correct
6. Gradients flow through identity embeddings + cross-attention
7. Fallback path (features disabled) still works
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import numpy as np
import tensorflow as tf
from src.agents.actor_critic_tf import (
    TCNFusionActor, TCNFusionCritic,
    ContextCrossAttentionBlock, create_actor_critic,
)

print("=" * 80)
print("CROSS-ASSET ATTENTION v2 VERIFICATION")
print("=" * 80)

NUM_ASSETS = 7
NUM_ACTIONS = NUM_ASSETS  # 7 assets (Dirichlet over 7)
PER_ASSET_DIM = 44
GLOBAL_DIM = 20
INPUT_DIM = NUM_ASSETS * PER_ASSET_DIM + GLOBAL_DIM
BATCH = 4
TIMESTEPS = 10
EMBED_DIM = 128

# =============================================================
# Test 1: ContextCrossAttentionBlock standalone
# =============================================================
print("\n--- Test 1: ContextCrossAttentionBlock Standalone ---")
ctx_block = ContextCrossAttentionBlock(d_model=EMBED_DIM, num_heads=4, name="test_ctx")
query = tf.random.normal((BATCH, NUM_ASSETS, EMBED_DIM))
context = tf.random.normal((BATCH, 1, EMBED_DIM))
out = ctx_block(query, context, training=True)
assert out.shape == (BATCH, NUM_ASSETS, EMBED_DIM), f"Shape mismatch: {out.shape}"
print(f"  Input:  query={query.shape}, context={context.shape}")
print(f"  Output: {out.shape}")
print("  ✅ ContextCrossAttentionBlock works")

# =============================================================
# Test 2: TCNFusionActor with ALL v2 features enabled
# =============================================================
print("\n--- Test 2: TCNFusionActor (all v2 features enabled) ---")
actor = TCNFusionActor(
    input_dim=INPUT_DIM,
    num_actions=NUM_ACTIONS,
    tcn_filters=[64, 128, 128],
    kernel_size=5,
    dilations=[2, 4, 8],
    dropout=0.2,
    num_assets=NUM_ASSETS,
    asset_feature_dim=PER_ASSET_DIM,
    global_feature_dim=GLOBAL_DIM,
    fusion_embed_dim=EMBED_DIM,
    fusion_attention_heads=4,
    fusion_dropout=0.1,
    fusion_cross_asset_mixer_enabled=True,
    fusion_cross_asset_mixer_layers=2,
    fusion_asset_identity_enabled=True,
    fusion_context_cross_attention_enabled=True,
    fusion_context_cross_attention_heads=4,
    fusion_context_cross_attention_dropout=0.1,
    fusion_per_asset_alpha_head=True,
    recurrent_memory_enabled=True,
    recurrent_memory_units=64,
    regime_conditioning_enabled=True,
)

# Test with structured dict input
asset_tensor = tf.random.normal((BATCH, TIMESTEPS, NUM_ASSETS, PER_ASSET_DIM))
context_tensor = tf.random.normal((BATCH, TIMESTEPS, GLOBAL_DIM))
state_dict = {"asset": asset_tensor, "context": context_tensor}

alpha_out = actor(state_dict, training=True)
print(f"  Dict input → alpha shape: {alpha_out.shape} (expected: ({BATCH}, {NUM_ACTIONS}))")
assert alpha_out.shape == (BATCH, NUM_ACTIONS), f"Actor output shape mismatch: {alpha_out.shape}"

# Test with flat tensor input (backward compat)
flat_state = tf.random.normal((BATCH, TIMESTEPS, INPUT_DIM))
alpha_flat = actor(flat_state, training=True)
print(f"  Flat input → alpha shape: {alpha_flat.shape} (expected: ({BATCH}, {NUM_ACTIONS}))")
assert alpha_flat.shape == (BATCH, NUM_ACTIONS), f"Actor flat output shape mismatch: {alpha_flat.shape}"

# Verify asset identity embed exists and is trainable
assert actor.asset_identity_embed is not None, "Asset identity embed missing!"
assert actor.asset_identity_embed.shape == (NUM_ASSETS, EMBED_DIM), f"Identity shape: {actor.asset_identity_embed.shape}"
print(f"  Asset identity embed shape: {actor.asset_identity_embed.shape}")
print(f"  Context cross-attn enabled: {actor.context_cross_attn_enabled}")
print(f"  Per-asset alpha head enabled: {actor.per_asset_alpha_head_enabled}")
assert actor.use_three_layer_context_stack, "Expected 3-layer context stack mode to be active"
print(f"  3-layer context stack active: {actor.use_three_layer_context_stack}")
print("  ✅ TCNFusionActor v2 works")

# =============================================================
# Test 3: TCNFusionCritic with ALL v2 features enabled
# =============================================================
print("\n--- Test 3: TCNFusionCritic (all v2 features enabled) ---")
critic = TCNFusionCritic(
    input_dim=INPUT_DIM,
    tcn_filters=[64, 128, 128],
    kernel_size=5,
    dilations=[2, 4, 8],
    dropout=0.2,
    num_assets=NUM_ASSETS,
    asset_feature_dim=PER_ASSET_DIM,
    global_feature_dim=GLOBAL_DIM,
    fusion_embed_dim=EMBED_DIM,
    fusion_attention_heads=4,
    fusion_dropout=0.1,
    fusion_cross_asset_mixer_enabled=True,
    fusion_cross_asset_mixer_layers=2,
    fusion_asset_identity_enabled=True,
    fusion_context_cross_attention_enabled=True,
    fusion_context_cross_attention_heads=4,
    fusion_context_cross_attention_dropout=0.1,
    recurrent_memory_enabled=True,
    recurrent_memory_units=64,
    regime_conditioning_enabled=True,
    distributional_critic_enabled=True,
    distributional_num_quantiles=17,
)

# Quantile output
value_out = critic(state_dict, training=True)
print(f"  Dict input → value shape: {value_out.shape} (expected: ({BATCH}, 17))")
assert value_out.shape == (BATCH, 17), f"Critic output shape mismatch: {value_out.shape}"

# Flat tensor
value_flat = critic(flat_state, training=True)
print(f"  Flat input → value shape: {value_flat.shape}")
assert value_flat.shape == (BATCH, 17)
print(f"  Critic identity embed shape: {critic.asset_identity_embed.shape}")
assert critic.use_three_layer_context_stack, "Expected critic 3-layer context stack mode to be active"
print(f"  Critic 3-layer context stack active: {critic.use_three_layer_context_stack}")
print("  ✅ TCNFusionCritic v2 works")

# =============================================================
# Test 4: Gradients flow through new layers
# =============================================================
print("\n--- Test 4: Gradient Flow Verification ---")
with tf.GradientTape() as tape:
    alpha = actor(state_dict, training=True)
    loss = tf.reduce_mean(alpha)
grads = tape.gradient(loss, actor.trainable_variables)

# Check identity embedding has gradients
identity_grads = [g for g, v in zip(grads, actor.trainable_variables) 
                  if 'asset_identity' in v.name and g is not None]
assert len(identity_grads) > 0, "No gradients for asset identity embedding!"
print(f"  ✅ Identity embedding has gradients (norm={tf.linalg.norm(identity_grads[0]).numpy():.6f})")

# Check cross-attention has gradients (check projection layer which is clearly named)
ctx_grads = [g for g, v in zip(grads, actor.trainable_variables) 
             if 'ctx_' in v.name and g is not None]
assert len(ctx_grads) > 0, "No gradients for context cross-attention!"
print(f"  ✅ Context cross-attention has gradients ({len(ctx_grads)} vars)")

per_asset_grads = [g for g, v in zip(grads, actor.trainable_variables)
                   if 'per_asset' in v.name and g is not None]
assert len(per_asset_grads) > 0, "No gradients for per-asset logit head!"
print(f"  ✅ Per-asset logit head has gradients ({len(per_asset_grads)} vars)")

none_grads = [v.name for g, v in zip(grads, actor.trainable_variables) if g is None]
if none_grads:
    print(f"  ⚠️  {len(none_grads)} vars with no gradient: {none_grads[:5]}")
else:
    print("  ✅ All trainable variables have gradients!")

# =============================================================
# Test 5: Backward compat — features disabled (legacy path)
# =============================================================
print("\n--- Test 5: Legacy Path (v2 features disabled) ---")
actor_legacy = TCNFusionActor(
    input_dim=INPUT_DIM,
    num_actions=NUM_ACTIONS,
    tcn_filters=[64, 128, 128],
    kernel_size=5,
    dilations=[2, 4, 8],
    dropout=0.2,
    num_assets=NUM_ASSETS,
    asset_feature_dim=PER_ASSET_DIM,
    global_feature_dim=GLOBAL_DIM,
    fusion_embed_dim=EMBED_DIM,
    fusion_cross_asset_mixer_enabled=False,
    fusion_asset_identity_enabled=False,
    fusion_context_cross_attention_enabled=False,
    fusion_per_asset_alpha_head=False,
    regime_conditioning_enabled=True,
)

alpha_legacy = actor_legacy(state_dict, training=False)
assert alpha_legacy.shape == (BATCH, NUM_ACTIONS)
assert actor_legacy.asset_identity_embed is None, "Identity should be None when disabled"
assert actor_legacy.context_cross_attn_block is None, "Cross-attn should be None when disabled"
assert actor_legacy.per_asset_logit_head is None, "Per-asset head should be None when disabled"
print(f"  ✅ Legacy path works: {alpha_legacy.shape}")

# =============================================================
# Test 6: Mixed-toggle combinations stay valid
# =============================================================
print("\n--- Test 6: Mixed-toggle combinations ---")
actor_ctx_only = TCNFusionActor(
    input_dim=INPUT_DIM,
    num_actions=NUM_ACTIONS,
    tcn_filters=[64, 128, 128],
    kernel_size=5,
    dilations=[2, 4, 8],
    dropout=0.2,
    num_assets=NUM_ASSETS,
    asset_feature_dim=PER_ASSET_DIM,
    global_feature_dim=GLOBAL_DIM,
    fusion_embed_dim=EMBED_DIM,
    fusion_cross_asset_mixer_enabled=True,
    fusion_asset_identity_enabled=True,
    fusion_context_cross_attention_enabled=True,
    fusion_per_asset_alpha_head=False,
    regime_conditioning_enabled=True,
)
alpha_ctx_only = actor_ctx_only(state_dict, training=False)
assert alpha_ctx_only.shape == (BATCH, NUM_ACTIONS)

actor_per_asset_only = TCNFusionActor(
    input_dim=INPUT_DIM,
    num_actions=NUM_ACTIONS,
    tcn_filters=[64, 128, 128],
    kernel_size=5,
    dilations=[2, 4, 8],
    dropout=0.2,
    num_assets=NUM_ASSETS,
    asset_feature_dim=PER_ASSET_DIM,
    global_feature_dim=GLOBAL_DIM,
    fusion_embed_dim=EMBED_DIM,
    fusion_cross_asset_mixer_enabled=True,
    fusion_asset_identity_enabled=True,
    fusion_context_cross_attention_enabled=False,
    fusion_per_asset_alpha_head=True,
    regime_conditioning_enabled=True,
)
alpha_per_asset_only = actor_per_asset_only(state_dict, training=False)
assert alpha_per_asset_only.shape == (BATCH, NUM_ACTIONS)
print("  ✅ Mixed-toggle actor paths work")

# =============================================================
# Test 7: Factory function works
# =============================================================
print("\n--- Test 7: create_actor_critic factory ---")
from src.config import PHASE1_CONFIG
cfg = PHASE1_CONFIG["agent_params"]
actor_f, critic_f = create_actor_critic("TCN_FUSION", INPUT_DIM, NUM_ACTIONS, cfg)
alpha_f = actor_f(state_dict, training=False)
value_f = critic_f(state_dict, training=False)
print(f"  Actor output:  {alpha_f.shape}")
print(f"  Critic output: {value_f.shape}")
assert alpha_f.shape == (BATCH, NUM_ACTIONS)
print("  ✅ Factory function works with v2 config")

# =============================================================
# Test 8: Parameter count comparison
# =============================================================
print("\n--- Test 8: Parameter Count ---")
actor_v2_params = sum(tf.size(v).numpy() for v in actor.trainable_variables)
actor_legacy_params = sum(tf.size(v).numpy() for v in actor_legacy.trainable_variables)
critic_params = sum(tf.size(v).numpy() for v in critic.trainable_variables)
print(f"  Actor v2 (all features):   {actor_v2_params:>10,} params")
print(f"  Actor legacy (no features): {actor_legacy_params:>10,} params")
print(f"  Critic v2:                  {critic_params:>10,} params")
print(f"  Actor overhead:             +{actor_v2_params - actor_legacy_params:,} params ({(actor_v2_params/actor_legacy_params - 1)*100:.1f}%)")

print("\n" + "=" * 80)
print("ALL TESTS PASSED ✅")
print("=" * 80)
