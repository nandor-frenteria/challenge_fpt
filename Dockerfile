# Use the official Python base image
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the port your Flask app will listen on
EXPOSE 5000

# Set the entry point command to run your Flask app
CMD ["python", "app.py"]
