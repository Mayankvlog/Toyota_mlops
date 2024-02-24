# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
#COPY . /app

# Update pip
#RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
#RUN pip install --no-cache-dir --disable-pip-version-check -r requirements.txt
#RUN pip install --no-cache-dir --disable-pip-version-check --no-parallel --quiet -r requirements.txt
RUN pip install --no-cache-dir --disable-pip-version-check --no-build-isolation -r requirements.txt
#RUN pip install --no-cache-dir --disable-pip-version-check --no-build-isolation --no-use-pep517 -r requirements.txt


# Make port 8501 available to the world outside this container
EXPOSE 8501

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["streamlit", "run", "app.py"]
