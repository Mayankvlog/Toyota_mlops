import pytest
from app import user_input_features, model

@pytest.mark.parametrize("slider_age, slider_km, slider_hp, checkbox_met_color, checkbox_automatic, slider_cc, slider_doors, slider_weight, select_fuel_type, expected_result", [
    (5, 50000, 100, False, False, 1500, 4, 1500, 'Petrol', {
        'Age': 5,
        'KM': 50000,
        'HP': 100,
        'MetColor': False,
        'Automatic': False,
        'CC': 1500,
        'Doors': 4,
        'Weight': 1500,
        'FuelType': 0  # Numeric value for 'Petrol'
    }),
])
def test_user_input_features(slider_age, slider_km, slider_hp, checkbox_met_color, checkbox_automatic, slider_cc, slider_doors, slider_weight, select_fuel_type, expected_result):
    with pytest.raises(Exception):  # Replace with your actual exception
        with patch('streamlit.sidebar.slider', side_effect=[slider_age, slider_km, slider_hp, slider_cc, slider_doors, slider_weight]):
            with patch('streamlit.sidebar.checkbox', side_effect=[checkbox_met_color, checkbox_automatic]):
                with patch('streamlit.sidebar.selectbox', return_value=select_fuel_type):
                    result = user_input_features()
                    assert result == expected_result

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

    # Simulate the expected prediction
    expected_prediction = 25000.0  

    # Make the prediction
    prediction = model.predict(input_features)
    assert prediction[0] == expected_prediction
