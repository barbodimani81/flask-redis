FROM python:3.11-alpine

# Set the working directory to /code
WORKDIR /code

# Copy requirements.txt into the container at /code
COPY requirements.txt code/requirements.txt

# Install the dependencies
RUN pip install -r code/requirements.txt

# Copy the rest of the application code to /code
COPY . .

# Command to run the Flask application
CMD ["python", "app.py"]