# Main Algorithm
Algorithm PetFoodDemandPrediction:
    Input: historical_data(2017-2022), external_factors
    Output: predictions(2024-2026)

# Core Functions
Function PreprocessData(data, factors):
    Clean and normalize data
    Engineer features
    Split train/test
    Return processed_data

Function BuildModels(data):
    # Linear Model
    linear_model = fit_MLR(
        target: pet_food_demand,
        features: [GDP, urbanization, pet_ownership, income]
    )
    
    # LSTM Model
    lstm_model = Sequential([
        LSTM(64, dropout=0.2),
        Dense(1)
    ])
    train(epochs=100, batch_size=32)
    
    Return linear_model, lstm_model

Function Predict(linear_model, lstm_model, test_data):
    Get predictions from both models
    final_pred = weighted_average(linear_pred, lstm_pred)
    Calculate metrics
    Return predictions, metrics

Function Visualize(predictions):
    Plot time series
    Plot regional distribution
    Return plots

# Main Execution
Main():
    data = load_data()
    processed = PreprocessData(data)
    models = BuildModels(processed)
    predictions = Predict(models)
    plots = Visualize(predictions)
    Export results