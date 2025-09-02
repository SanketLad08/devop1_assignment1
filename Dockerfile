FROM python:3.12-slim

# Install system deps: Tkinter + Xvfb
RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt pytest

# Copy source code
COPY . .

# Run pytest in a virtual display when container starts
CMD ["xvfb-run", "-a", "pytest", "-v"]
