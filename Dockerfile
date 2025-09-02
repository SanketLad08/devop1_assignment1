FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Add app root to PYTHONPATH
ENV PYTHONPATH=/app

CMD ["pytest", "-v"]
