 Router audit rows (multi-expert only): 203
Stage coverage: {'B_ramp_1': 56, 'B_ramp_2': 40, 'C_disc_intro': 40, 'C_ramp_2': 36, 'C_full_tape': 31}
Direct router-input features found in log: ['snapshot_drawdown_current', 'episode_turnover_pct']
Average router weights by phase

  
    

    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }


  
    
      
      router_return
      router_risk
      router_discipline
    
    
      phase_label
      
      
      
    
  
  
    
      B_ramp_1
      0.719
      0.281
      0.000
    
    
      B_ramp_2
      0.638
      0.362
      0.000
    
    
      C_disc_intro
      0.335
      0.454
      0.211
    
    
      C_full_tape
      0.343
      0.411
      0.246
    
    
      C_ramp_2
      0.330
      0.426
      0.245
    
  


    

  
    

  
    
  
    

  
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  

    
      const buttonEl =
        document.querySelector('#df-4e874a60-ca51-459b-b07c-5ce368bd37be button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-4e874a60-ca51-459b-b07c-5ce368bd37be');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    
  


    
  
Overall feature correlations with router_risk

  
    

    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }


  
    
      
      spearman_corr_with_router_risk
    
  
  
    
      snapshot_drawdown_current
      0.159
    
    
      episode_turnover_pct
      0.561
    
  


    

  
    

  
    
  
    

  
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  

    
      const buttonEl =
        document.querySelector('#df-209db744-8e84-4212-bfa0-98573399efdf button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-209db744-8e84-4212-bfa0-98573399efdf');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    
  


    
  
Phase-separated feature correlations with router_risk

  
    

    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }


  
    
      
      phase_label
      feature
      spearman_corr_with_router_risk
    
  
  
    
      0
      B_ramp_1
      snapshot_drawdown_current
      0.097
    
    
      1
      B_ramp_1
      episode_turnover_pct
      -0.153
    
    
      2
      B_ramp_2
      snapshot_drawdown_current
      0.136
    
    
      3
      B_ramp_2
      episode_turnover_pct
      0.083
    
    
      4
      C_disc_intro
      snapshot_drawdown_current
      0.105
    
    
      5
      C_disc_intro
      episode_turnover_pct
      0.170
    
    
      6
      C_full_tape
      snapshot_drawdown_current
      -0.262
    
    
      7
      C_full_tape
      episode_turnover_pct
      0.388
    
    
      8
      C_ramp_2
      snapshot_drawdown_current
      -0.139
    
    
      9
      C_ramp_2
      episode_turnover_pct
      -0.345
    
  


    

  
    

  
    
  
    

  
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  

    
      const buttonEl =
        document.querySelector('#df-1a05f36b-8209-452b-a24d-19af6d92e158 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-1a05f36b-8209-452b-a24d-19af6d92e158');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    
  


    
  
Bucketed average router weights by feature level

  
    

    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }


  
    
      
      feature_bucket
      feature
      router_return
      router_risk
      router_discipline
    
  
  
    
      0
      low
      snapshot_drawdown_current
      0.537
      0.360
      0.103
    
    
      1
      mid
      snapshot_drawdown_current
      0.512
      0.378
      0.110
    
    
      2
      high
      snapshot_drawdown_current
      0.455
      0.392
      0.153
    
    
      3
      low
      episode_turnover_pct
      0.688
      0.300
      0.011
    
    
      4
      mid
      episode_turnover_pct
      0.478
      0.411
      0.111
    
    
      5
      high
      episode_turnover_pct
      0.336
      0.419
      0.245
    
  


    

  
    

  
    
  
    

  
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  

    
      const buttonEl =
        document.querySelector('#df-f860cb9e-f642-4015-8493-9e204ffb3700 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-f860cb9e-f642-4015-8493-9e204ffb3700');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    
  


    
  
Rolling-window audit using feature: snapshot_drawdown_current | window=10

  
    

    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }


  
    
      
      update
      phase_label
      router_risk
      snapshot_drawdown_current
      rolling_router_risk_mean
      rolling_feature_mean
      rolling_spearman
    
  
  
    
      183
      382
      C_full_tape
      0.355
      0.045
      0.425
      0.102
      0.079
    
    
      184
      383
      C_full_tape
      0.339
      0.078
      0.426
      0.092
      0.370
    
    
      185
      384
      C_full_tape
      0.317
      0.185
      0.416
      0.096
      0.067
    
    
      186
      385
      C_full_tape
      0.315
      0.184
      0.403
      0.099
      -0.139
    
    
      187
      386
      C_full_tape
      0.317
      0.232
      0.390
      0.107
      -0.345
    
    
      188
      387
      C_full_tape
      0.343
      0.186
      0.377
      0.104
      -0.661
    
    
      189
      388
      C_full_tape
      0.386
      0.177
      0.364
      0.111
      -0.806
    
    
      190
      389
      C_full_tape
      0.424
      0.153
      0.361
      0.126
      -0.648
    
    
      191
      390
      C_full_tape
      0.427
      0.165
      0.363
      0.142
      -0.539
    
    
      192
      391
      C_full_tape
      0.488
      0.192
      0.371
      0.160
      -0.164
    
    
      193
      392
      C_full_tape
      0.483
      0.193
      0.384
      0.174
      0.079
    
    
      194
      393
      C_full_tape
      0.463
      0.128
      0.396
      0.179
      -0.067
    
    
      195
      394
      C_full_tape
      0.477
      0.071
      0.412
      0.168
      -0.164
    
    
      196
      395
      C_full_tape
      0.532
      0.049
      0.434
      0.155
      -0.406
    
    
      197
      396
      C_full_tape
      0.479
      0.032
      0.450
      0.135
      -0.188
    
    
      198
      397
      C_full_tape
      0.484
      0.071
      0.464
      0.123
      -0.212
    
    
      199
      398
      C_full_tape
      0.445
      0.162
      0.470
      0.122
      -0.188
    
    
      200
      399
      C_full_tape
      0.376
      0.140
      0.465
      0.120
      -0.188
    
    
      201
      400
      C_full_tape
      0.380
      0.136
      0.461
      0.117
      -0.188
    
    
      202
      401
      C_full_tape
      0.357
      0.021
      0.448
      0.100
      -0.067
    
  


    

  
    

  
    
  
    

  
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  

    
      const buttonEl =
        document.querySelector('#df-6a5f2194-4bb3-426b-b4ff-6a8736c6a112 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-6a5f2194-4bb3-426b-b4ff-6a8736c6a112');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    
  


    
  
Latest router rows

  
    

    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }


  
    
      
      update
      timestep
      phase_label
      router_return
      router_risk
      router_discipline
    
  
  
    
      188
      387
      472752
      C_full_tape
      0.380121
      0.343183
      0.276696
    
    
      189
      388
      474768
      C_full_tape
      0.355833
      0.385928
      0.258240
    
    
      190
      389
      476784
      C_full_tape
      0.320985
      0.423930
      0.255085
    
    
      191
      390
      478800
      C_full_tape
      0.318581
      0.427299
      0.254120
    
    
      192
      391
      480816
      C_full_tape
      0.305755
      0.488244
      0.206001
    
    
      193
      392
      482832
      C_full_tape
      0.312807
      0.482731
      0.204462
    
    
      194
      393
      484848
      C_full_tape
      0.334448
      0.462971
      0.202581
    
    
      195
      394
      486864
      C_full_tape
      0.329145
      0.476747
      0.194109
    
    
      196
      395
      488880
      C_full_tape
      0.291227
      0.532491
      0.176281
    
    
      197
      396
      490896
      C_full_tape
      0.314456
      0.478520
      0.207024
    
    
      198
      397
      492912
      C_full_tape
      0.309483
      0.484304
      0.206213
    
    
      199
      398
      494928
      C_full_tape
      0.316406
      0.445138
      0.238456
    
    
      200
      399
      496944
      C_full_tape
      0.363656
      0.376424
      0.259920
    
    
      201
      400
      498960
      C_full_tape
      0.365380
      0.379931
      0.254689
    
    
      202
      401
      500000
      C_full_tape
      0.383915
      0.357137
      0.258948
    
  


    

  
    

  
    
  
    

  
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  

    
      const buttonEl =
        document.querySelector('#df-9289c80c-e666-4644-83ba-b579c662577e button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-9289c80c-e666-4644-83ba-b579c662577e');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    
  


    
  
