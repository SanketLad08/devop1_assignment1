FROM python:3.12-slim

# Set workdir
WORKDIR /app

# Copy everything
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command runs tests (safe for CI)
CMD ["pytest", "-v"]
