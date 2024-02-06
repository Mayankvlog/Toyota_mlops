import pytest
import pandas as pd
import streamlit as st
from app import user_input_features

def test_user_input_features():
    # Mocking st.sidebar.slider with specific values
    st.sidebar.slider = lambda label, min_value, max_value, value: {
        'Age': 5,
        'KM': 50000,
        'HP': 100,
        'CC': 1500,
        'Doors': 4,
        'Weight': 1500
    }[label]

    # Call the function and check if it returns the expected DataFrame
    result = user_input_features()
    expected_result = pd.DataFrame({
        'Age': [5],
        'KM': [50000],
        'HP': [100],
        'MetColor': [False],
        'Automatic': [False],
        'CC': [1500],
        'Doors': [4],
        'Weight': [1500],
        'FuelType': [0]  # Assuming the default selection is 'Petrol'
    })

    pd.testing.assert_frame_equal(result, expected_result)
