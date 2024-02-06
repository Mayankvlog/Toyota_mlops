import pytest
import pandas as pd
import streamlit as st
from app import user_input_features

def test_user_input_features():
    # You might need to mock some Streamlit components if needed
    # For simplicity, let's assume st.sidebar.slider always returns 5
    st.sidebar.slider = lambda *args, **kwargs: 5

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

