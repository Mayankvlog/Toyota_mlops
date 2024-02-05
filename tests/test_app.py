# tests/test_app.py
import pytest
from ..app import user_input_features, predict_price

# Mocking a sample DataFrame
@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'Age': [5],
        'KM': [50000],
        'HP': [100],
        'MetColor': [False],
        'Automatic': [False],
        'CC': [1500],
        'Doors': [4],
        'Weight': [1500],
        'FuelType': [0]
    })

# Test the user_input_features function
def test_user_input_features(sample_df):
    with st.sidebar:
        st.slider = lambda label, min_value, max_value, value: sample_df[label.lower()][0]
        st.checkbox = lambda label: sample_df[label.lower()][0]
        st.selectbox = lambda label, options: options[sample_df[label.lower()][0]]
        features = user_input_features()
    assert features.equals(sample_df)

# Test the predict_price function
def test_predict_price(sample_df):
    model = RandomForestRegressor()
    model.fit(X_train, y_train)  # Assuming you have X_train and y_train defined
    with mlflow.start_run():
        mlflow.log_param("Model", "Random Forest")
        mlflow.log_param("Age", sample_df['Age'][0])
        mlflow.log_param("KM", sample_df['KM'][0])
        mlflow.log_param("HP", sample_df['HP'][0])
        mlflow.log_param("MetColor", sample_df['MetColor'][0])
        mlflow.log_param("Automatic", sample_df['Automatic'][0])
        mlflow.log_param("CC", sample_df['CC'][0])
        mlflow.log_param("Doors", sample_df['Doors'][0])
        mlflow.log_param("Weight", sample_df['Weight'][0])
        mlflow.log_metric("PredictedPrice", predict_price(model, sample_df)[0])

    # Log to file
    logging.info(f"Prediction: {prediction[0]:,.2f}")
