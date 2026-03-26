 Router audit rows (multi-expert only): 85
Stage coverage: {'B_ramp_1': 40, 'B_ramp_2': 37, 'C_ramp_1': 8}
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
      0.725
      0.275
      0.00
    
    
      B_ramp_2
      0.640
      0.360
      0.00
    
    
      C_ramp_1
      0.530
      0.240
      0.23
    
  


    

  
    

  
    
  
    

  
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
        document.querySelector('#df-826cd265-4b08-471c-9a25-6c495f2a9b27 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-826cd265-4b08-471c-9a25-6c495f2a9b27');
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
      -0.152
    
    
      episode_turnover_pct
      -0.021
    
  


    

  
    

  
    
  
    

  
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
        document.querySelector('#df-934cab75-317b-4605-b495-cd5a66eac560 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-934cab75-317b-4605-b495-cd5a66eac560');
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
      -0.291
    
    
      1
      B_ramp_1
      episode_turnover_pct
      -0.182
    
    
      2
      B_ramp_2
      snapshot_drawdown_current
      -0.140
    
    
      3
      B_ramp_2
      episode_turnover_pct
      -0.532
    
    
      4
      C_ramp_1
      snapshot_drawdown_current
      0.071
    
    
      5
      C_ramp_1
      episode_turnover_pct
      0.357
    
  


    

  
    

  
    
  
    

  
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
        document.querySelector('#df-c802c7d5-fb6b-49fc-938f-0f5f692f1699 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-c802c7d5-fb6b-49fc-938f-0f5f692f1699');
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
      0.662
      0.312
      0.025
    
    
      1
      mid
      snapshot_drawdown_current
      0.660
      0.315
      0.025
    
    
      2
      high
      snapshot_drawdown_current
      0.686
      0.299
      0.015
    
    
      3
      low
      episode_turnover_pct
      0.699
      0.301
      0.000
    
    
      4
      mid
      episode_turnover_pct
      0.669
      0.331
      0.000
    
    
      5
      high
      episode_turnover_pct
      0.640
      0.294
      0.066
    
  


    

  
    

  
    
  
    

  
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
        document.querySelector('#df-4119d0af-3dab-408a-8717-e96fe90d3fe7 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-4119d0af-3dab-408a-8717-e96fe90d3fe7');
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
    
  
  
    
      65
      247
      B_ramp_2
      0.369
      0.000
      0.376
      0.008
      0.377
    
    
      66
      248
      B_ramp_2
      0.371
      0.044
      0.378
      0.012
      0.274
    
    
      67
      249
      B_ramp_2
      0.349
      0.016
      0.377
      0.012
      0.164
    
    
      68
      250
      B_ramp_2
      0.359
      0.000
      0.373
      0.011
      0.313
    
    
      69
      251
      B_ramp_2
      0.344
      0.096
      0.369
      0.020
      -0.031
    
    
      70
      252
      B_ramp_2
      0.347
      0.122
      0.366
      0.030
      -0.374
    
    
      71
      253
      B_ramp_2
      0.353
      0.064
      0.362
      0.036
      -0.546
    
    
      72
      254
      B_ramp_2
      0.314
      0.099
      0.357
      0.046
      -0.669
    
    
      73
      255
      B_ramp_2
      0.277
      0.086
      0.346
      0.053
      -0.767
    
    
      74
      256
      B_ramp_2
      0.273
      0.003
      0.336
      0.053
      -0.426
    
    
      75
      257
      B_ramp_2
      0.303
      0.005
      0.329
      0.054
      -0.079
    
    
      76
      258
      B_ramp_2
      0.305
      0.040
      0.322
      0.053
      0.018
    
    
      77
      259
      C_ramp_1
      0.255
      0.052
      0.313
      0.057
      0.164
    
    
      78
      260
      C_ramp_1
      0.235
      0.015
      0.300
      0.058
      0.636
    
    
      79
      261
      C_ramp_1
      0.252
      0.004
      0.291
      0.049
      0.636
    
    
      80
      262
      C_ramp_1
      0.243
      0.011
      0.281
      0.038
      0.515
    
    
      81
      263
      C_ramp_1
      0.225
      0.000
      0.268
      0.032
      0.576
    
    
      82
      264
      C_ramp_1
      0.233
      0.063
      0.260
      0.028
      0.212
    
    
      83
      265
      C_ramp_1
      0.242
      0.008
      0.256
      0.020
      0.030
    
    
      84
      266
      C_ramp_1
      0.239
      0.028
      0.253
      0.023
      0.091
    
  


    

  
    

  
    
  
    

  
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
        document.querySelector('#df-99a47e20-d516-438d-9877-e94c8c7bb150 button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-99a47e20-d516-438d-9877-e94c8c7bb150');
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
    
  
  
    
      70
      252
      307440
      B_ramp_2
      0.652534
      0.347466
      0.000000
    
    
      71
      253
      309456
      B_ramp_2
      0.646829
      0.353171
      0.000000
    
    
      72
      254
      311472
      B_ramp_2
      0.686390
      0.313610
      0.000000
    
    
      73
      255
      313488
      B_ramp_2
      0.723227
      0.276773
      0.000000
    
    
      74
      256
      315504
      B_ramp_2
      0.727407
      0.272593
      0.000000
    
    
      75
      257
      317520
      B_ramp_2
      0.697038
      0.302962
      0.000000
    
    
      76
      258
      319536
      B_ramp_2
      0.695226
      0.304774
      0.000000
    
    
      77
      259
      321552
      C_ramp_1
      0.567849
      0.255224
      0.176926
    
    
      78
      260
      323568
      C_ramp_1
      0.553350
      0.234641
      0.212009
    
    
      79
      261
      325584
      C_ramp_1
      0.540609
      0.251993
      0.207398
    
    
      80
      262
      327600
      C_ramp_1
      0.519672
      0.242854
      0.237474
    
    
      81
      263
      329616
      C_ramp_1
      0.529794
      0.224786
      0.245420
    
    
      82
      264
      331632
      C_ramp_1
      0.518813
      0.232813
      0.248374
    
    
      83
      265
      333648
      C_ramp_1
      0.500830
      0.242346
      0.256824
    
    
      84
      266
      335664
      C_ramp_1
      0.506335
      0.239250
      0.254416
    
  


    

  
    

  
    
  
    

  
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
        document.querySelector('#df-22f940dd-fed5-47dc-a39d-87133cac78ca button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-22f940dd-fed5-47dc-a39d-87133cac78ca');
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
    
  


    
  
