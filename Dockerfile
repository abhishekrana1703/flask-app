# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the dependencies
RUN pip install -r requirements.txt

# Copy the Flask application into the container
COPY app.py app.py

# Expose port 5000 for the Flask application
EXPOSE 5000

# Define the command to run the Flask application
CMD ["python", "app.py"]
