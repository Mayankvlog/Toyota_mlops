# Toyota_dvc
Features of the app

To enter automobile specs like age, miles, horsepower, and so on, drag and drop sliders and checkboxes on the sidebar.
Predictive Model
Choose between the Random Forest, k-NN, SVR, and linear regression models on the sidebar.


Based on the user's input, the predicted automobile price is shown.



Model tracking is done using MLOps Integration MLflow.
Using Pickle, trained models are stored in the models/ directory.
Displays


The dataset may be understood through the use of scatter, pie, bar, and line plots.


Monitoring MLflow
The MLflow user interface (UI) tracks model artifacts and shows experiment details.


ML development together using the DAGsHub Repository.
Participating
Create a pull request after making modifications to the repository by forking it.
To discuss proposed adjustments for substantial changes, please start an issue.
MLFLOW_TRACKING_URI=https://dagshub.com/Mayankvlog/Toyota_mlops.mlflow \
MLFLOW_TRACKING_USERNAME=Mayankvlog \
MLFLOW_TRACKING_PASSWORD=a163dc11889cf8831384598f795e7c53cd54b1d2 \
streamlit run app.py


