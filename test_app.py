import pytest
import numpy as np
from app import user_input_features, model

def test_prediction_logic():
    # Simulate prediction logic test
    # You may need to adjust this based on your actual model logic

    # Simulate input features
    input_features = {
        'Age': 5,
        'KM': 50000,
        'HP': 100,
        'MetColor': False,
        'Automatic': False,
        'CC': 1500,
        'Doors': 4,
        'Weight': 1500,
        'FuelType': 0  # Numeric value for 'Petrol'
    }

    # Convert input_features to a NumPy array
    input_array = np.array([[input_features[key] for key in input_features]])


    # Simulate the expected prediction
    expected_prediction = 25000.0  

    # Make the prediction
    prediction = model.predict(input_features)
    assert prediction[0] == expected_prediction
