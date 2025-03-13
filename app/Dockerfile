FROM alpine:latest

RUN apk add --no-cache python3 py3-pip && \
    pip install --no-cache-dir --upgrade pip

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD while true; do python3 api.py || sleep 5; done
