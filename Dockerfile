FROM python:3.12-slim

# Install Tkinter + Xvfb + fonts (needed for Tk)
RUN apt-get update && apt-get install -y \
    python3-tk \
    xvfb \
    x11-utils \
    fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt pytest

COPY . .

# Run pytest in a virtual display
ENTRYPOINT ["xvfb-run", "-a"]
CMD ["pytest", "-v", "--maxfail=1", "--disable-warnings"]
