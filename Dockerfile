# Start from Alpine Linux
FROM alpine:latest

# Install Python3, pip, gcc (for building some Python packages), and other dependencies
RUN apk add --no-cache \
    gcc \
    mysql-client \
    python3 \
    py3-pip \
    libc-dev \
    libffi-dev

# Copy in requirements to install Python dependencies
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --break-system-packages -r /app/requirements.txt

# Create a non-root user and a directory for the app
RUN addgroup -S appgroup && \
    adduser -S -G appgroup appuser && \
    mkdir /app && \
    chown appuser:appgroup /app

# Switch to the new user and set the working directory
USER appuser
WORKDIR /app

# Copy your Flask app into the container
COPY --chown=appuser:appgroup app.py /app/

# Expose the port Flask listens on
EXPOSE 5000

# Start the Flask app
ENTRYPOINT ["/usr/bin/python3", "/app/app.py"]
