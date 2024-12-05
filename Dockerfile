<<<<<<< HEAD
# Dockerfile for GrowBot
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files to the container
COPY . /app

# Install dependencies


# Expose port 5000 for the Flask application
EXPOSE 5000

# Start the application
CMD ["python", "run.py"]
=======
# Use Python as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /bot

# Copy bot files to the container
COPY bot/ /bot/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (if needed for bot webhook)
EXPOSE 8443

# Set environment variables (replace placeholders with real values)
ENV TELEGRAM_TOKEN=7586067879:AAFtBcPcu8_eQYVmUqmpDltASX7TLZObwkI
ENV TELEGRAM_WEBHOOK_URL=https://your-webhook-url/

# Run the bot
CMD ["python", "-m", "web.app"]
>>>>>>> 1c802b13 (Updated project files and features.)
