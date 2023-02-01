# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the contents of the current directory to the container
COPY app.py .
COPY requirements.txt .
COPY templates/html/form.html templates/html/
COPY templates/html/home.html templates/html/
COPY static/style.css static/

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python", "app.py"]
