# Base image
FROM python:3.12-slim

# Install Tkinter dependencies
RUN apt-get update && apt-get install -y \
    python3-tk \
    tk \
    tcl \
    libtk8.6 \
    && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run pytest by default
CMD ["pytest", "-v"]
