# Use a lightweight base image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install dependencies for PyTorch CPU and pip
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install PyTorch CPU from the specified URL
RUN pip install --no-cache-dir torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

# Copy backend requirements
COPY backend/requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend files
COPY artefacts /app/artefacts

# Copy backend files
COPY backend /app/backend

# Install slanggen from the wheel file
COPY dist/slanggen*.whl /app/
RUN pip install --no-cache-dir slanggen*.whl

# Expose port 80 for the application
# EXPOSE 80
WORKDIR backend

# Determine the application entry point (replace with the correct entry point based on backend/app.py)
CMD ["python", "app.py"]
