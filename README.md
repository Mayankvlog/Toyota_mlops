# Toyota_mlops
#   Features of the app

The gave code scrap is a Streamlit web application at foreseeing Toyota vehicle costs in light of client input boundaries, for example, age, kilometers driven, strength, and so on. Here is a breakdown of the usefulness:

Client Info Boundaries: Clients can enter different boundaries, for example, age, kilometers driven, pull, and so on, utilizing sliders and checkboxes in the sidebar.

Model Determination: Clients can choose one of the accessible AI models (Irregular Woodland, k-NN, SVR, Direct Relapse) from the sidebar.

Expectation: After choosing the model, the application predicts the vehicle cost in light of the client input boundaries utilizing the picked model.

Perception: The application gives representations, for example, disperse plots, pie plots, bar plots, and line plots in light of the Toyota dataset. These representations assist clients with figuring out the information circulation and examples.

MLflow Joining: The application logs boundaries, measurements, and ancient rarities utilizing MLflow, empowering following and reproducibility of AI tests.

Testing: Unit tests are incorporated to confirm the usefulness of the user_input_features capability.

Docker Setup: The application is containerized utilizing Docker, and there are designs for building and sending the Docker picture to DockerHub.


CI/CD Workflow: Continuous integration and continuous deployment (CI/CD) workflows are defined using CircleCI, ensuring automated testing and deployment of the application.

To work on the application, you could consider:

Improving the UI with better styling and design.
Executing further developed AI models and assessing their exhibition.
Adding more perceptions and intuitive parts to investigate the information.
Consolidating mistake taking care of and approval for client input.
Streamlining the Docker picture size and working on the CI/CD pipeline setup.
Generally, the application gives a thorough answer for anticipating Toyota vehicle costs and picturing the dataset, alongside hearty testing and sending work processes.                  
#   Run cammands 
docker run -d -p 8501:80 mayank035/toyotaapp:latest


docker ps -a

docker logs $Cointainer_id

