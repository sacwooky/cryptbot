# Use an official Python runtime with additional system dependencies
FROM python:3.9-slim

# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Set proper file permissions (fixes Unraid permission issues)
RUN chmod -R 777 /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for security
ENV POSTGRES_PASSWORD=""
ENV POSTGRES_HOST="localhost"
ENV POSTGRES_PORT="5432"
ENV TELEGRAM_BOT_TOKEN=""
ENV TELEGRAM_CHAT_ID=""

# Run the bot script when the container launches
CMD ["python", "bot.py"]
