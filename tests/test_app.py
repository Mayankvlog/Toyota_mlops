import unittest
from unittest.mock import patch
from app import user_input_features

class TestStreamlitApp(unittest.TestCase):
    @patch('streamlit.sidebar.slider', return_value=5)
    @patch('streamlit.sidebar.slider', return_value=50000)
    @patch('streamlit.sidebar.slider', return_value=100)
    @patch('streamlit.sidebar.checkbox', return_value=False)
    @patch('streamlit.sidebar.checkbox', return_value=False)
    @patch('streamlit.sidebar.slider', return_value=1500)
    @patch('streamlit.sidebar.slider', return_value=4)
    @patch('streamlit.sidebar.slider', return_value=1500)
    @patch('streamlit.sidebar.selectbox', return_value='Petrol')
    def test_user_input_features(self, slider_age, slider_km, slider_hp, checkbox_met_color,
                                 checkbox_automatic, slider_cc, slider_doors, slider_weight, select_fuel_type):
        # Simulate a user input feature test
        expected_result = {
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
        result = user_input_features()
        self.assertEqual(result, expected_result)

    def test_prediction_logic(self):
        # Simulate prediction logic test
        # You may need to adjust this based on your actual model logic
        from your_streamlit_app_file import model  # Import the actual model from your app file

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
        expected_prediction = 25000.0  # Replace with the expected prediction for your model

        # Make the prediction
        prediction = model.predict(input_features)
        self.assertEqual(prediction[0], expected_prediction)

if __name__ == '__main__':
    unittest.main()

