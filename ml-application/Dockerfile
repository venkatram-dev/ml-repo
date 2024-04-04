# Use Python 3.11.4 as the base image
FROM python:3.11.4-slim

# Set the working directory to /app in the Docker container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Update the CMD to reflect the correct location of your Flask app within the 'app' package
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app.main:app"]
