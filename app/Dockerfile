FROM alpine:latest

#Installs python and pip 
RUN apk add --no-cache  gcc \
            python3 \
            py3-pip \
            libc-dev \
            libffi-dev
COPY requirements.txt .

RUN pip install -r requirements.txt

RUN addgroup -S appgroup && \
    adduser -S -G appgroup appuser && \
    mkdir /app && \
    chown appuser /app

USER appuser
WORKDIR /app

#COPY api.py .
COPY --chown=appuser:appgroup api.py .

EXPOSE 5000

# TODO: run your service here
ENTRYPOINT ["/usr/bin/python3", "/app/api.py"]
