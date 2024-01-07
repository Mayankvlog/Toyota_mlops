import streamlit as st 
import pandas as pd
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn
import pickle
import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO)

# Load Toyota dataset
data = pd.read_csv('data/Toyota.csv')

# Set page layout
st.set_page_config(
    page_title="Toyota MLOps Project",
    page_icon=":car:",
    layout="wide",
)

# Add logo to the top right corner
logo_path = "toyota.jpg"
st.image(logo_path, width=150)

# Sidebar for user input parameters
st.sidebar.header('Input')

def user_input_features():
    age = st.sidebar.slider('Age', min_value=0, max_value=60, value=5)
    km = st.sidebar.slider('KM', min_value=5000, max_value=200000, value=50000)
    hp = st.sidebar.slider('HP', min_value=50, max_value=200, value=100)
    met_color = st.sidebar.checkbox('Metallic Color')
    automatic = st.sidebar.checkbox('Automatic Transmission')
    cc = st.sidebar.slider('CC', min_value=1000, max_value=3000, value=1500)
    doors = st.sidebar.slider('Number of Doors', min_value=2, max_value=5, value=4)
    weight = st.sidebar.slider('Weight', min_value=800, max_value=2500, value=1500)

    fuel_types = ['Petrol', 'Diesel', 'CNG']
    fuel_type_selection = st.sidebar.selectbox('Fuel Type', fuel_types).lower()

    # Convert categorical FuelType to numerical
    fuel_type_mapping = {'petrol': 0, 'diesel': 1, 'cng': 2}
    fuel_type = fuel_type_mapping.get(fuel_type_selection, 0)

    data = {
        'Age': age,
        'KM': km,
        'HP': hp,
        'MetColor': met_color,
        'Automatic': automatic,
        'CC': cc,
        'Doors': doors,
        'Weight': weight,
        'FuelType': fuel_type  # Use the numerical representation
    }

    features = pd.DataFrame(data, index=[0])
    return features

# Main app content
st.write("""
# Toyota Car Price Prediction App
This app predicts the **Toyota car price** based on user input parameters!
""")

# Sidebar - User input features
df = user_input_features()

# Display user input parameters
st.subheader('User Input Parameters')
st.write(df)

# Split data into features and target
X = data.drop('Price', axis=1)
y = data['Price']

# One-hot encode the 'FuelType' column
X = pd.get_dummies(X, columns=['FuelType'], drop_first=True)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Models
models = {
    'Random Forest': RandomForestRegressor(),
    'k-NN': KNeighborsRegressor(),
    'SVR': SVR(),
    'Linear Regression': LinearRegression()
}

# User selects a model
selected_model = st.sidebar.selectbox('Select Model', list(models.keys()))

# Initialize the selected model
model = models[selected_model]

# Train the model
model.fit(X_train, y_train)

# Ensure input features match training features
df = pd.get_dummies(df, columns=['FuelType'], drop_first=True)
df = df.reindex(columns=X.columns, fill_value=0)

# Make predictions
prediction = model.predict(df)

# Display prediction
st.subheader('Predicted Car Price')
st.write(f"${prediction[0]:,.2f}")

# Save the trained model using pickle
model_filename = f'models/{selected_model.lower()}_model.pkl'
with open(model_filename, 'wb') as model_file:
    pickle.dump(model, model_file)

# Log parameters and metrics with MLflow
experiment_name = "my_experiment"  # Replace with your experiment name

# Set the experiment
mlflow.set_experiment(experiment_name)

# Log parameters and metrics with MLflow
if mlflow.active_run() is None:
   with mlflow.start_run():
      mlflow.log_param("Model", selected_model)
      mlflow.log_param("Age", df['Age'][0])
      mlflow.log_param("KM", df['KM'][0])
      mlflow.log_param("HP", df['HP'][0])
      mlflow.log_param("MetColor", df['MetColor'][0])
      mlflow.log_param("Automatic", df['Automatic'][0])
      mlflow.log_param("CC", df['CC'][0])
      mlflow.log_param("Doors", df['Doors'][0])
      mlflow.log_param("Weight", df['Weight'][0])
      mlflow.log_metric("PredictedPrice", prediction[0])

    # Log to file
      logging.info(f"Prediction: {prediction[0]:,.2f}")


    # Log metrics to MLflow
    # Define values for additional metrics
      value1 = 42  # Replace with the actual value for AdditionalMetric1
      value2 = 23.5  # Replace with the actual value for AdditionalMetric2

    # Log metrics to MLflow
    # Log additional metrics if needed
      mlflow.log_metric("AdditionalMetric1", value1)
      mlflow.log_metric("AdditionalMetric2", value2)


    

# Visualization
st.subheader("Visualization")

# Scatter Plot
st.subheader("Scatter Plot:")
scatter_fig = px.scatter(data, x='Age', y='Price', color='FuelType')
st.plotly_chart(scatter_fig)

# Pie Plot
st.subheader("Pie Plot:")
pie_fig = px.pie(data, names='FuelType')
st.plotly_chart(pie_fig)

# Bar Plot
st.subheader("Bar Plot:")
bar_fig = px.bar(data, x='Doors', y='Price', color='FuelType')
st.plotly_chart(bar_fig)

# Line Plot
st.subheader("Line Plot:")
line_fig = px.line(data, x='KM', y='Price', color='FuelType')
st.plotly_chart(line_fig)

# Save plots as artifacts
scatter_fig.write_html("scatter_plot.html")
mlflow.log_artifact("scatter_plot.html")

pie_fig.write_html("pie_plot.html")
mlflow.log_artifact("pie_plot.html")

bar_fig.write_html("bar_plot.html")
mlflow.log_artifact("bar_plot.html")

line_fig.write_html("line_plot.html")
mlflow.log_artifact("line_plot.html")

mlflow.end_run()

# Link to DAGsHub Repository
st.markdown("[DAGsHub Repository](https://dagshub.com/Mayankvlog/Toyota_mlops.mlflow)")
