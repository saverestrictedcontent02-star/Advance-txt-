FROM python:3.10-slim

# System dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    aria2 \
    gcc \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Work directory
WORKDIR /app

# Copy files
COPY . .

# Upgrade pip
RUN pip install --upgrade pip

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Extra dependency (repo me use ho rahi hai)
RUN pip install pytube

# Environment variable
ENV COOKIES_FILE_PATH=youtube_cookies.txt

# Start bot
CMD ["python", "main.py"]