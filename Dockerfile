# Use a base Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory (.) content into the container's /app directory
COPY . /app

# Install the necessary dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your app will run on
EXPOSE 8080

# Command to run the application (replace 'app.py' with your main script)
CMD ["python", "app.py"]
