# Dockerfile for GrowBot
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for the Flask application
EXPOSE 5000

# Start the application
CMD ["python", "run.py"]
