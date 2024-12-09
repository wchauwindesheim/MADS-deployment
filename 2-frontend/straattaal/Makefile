# Variables
WHEEL_FILE = ./dist/slanggen*.whl
MODEL_FILE = ./artefacts/model.pth
DOCKER_IMAGE = straattaal-backend
PORT = 8080

# Default target
all: run

# Help target
help:
	@echo "Available targets:"
	@echo "  all       - Default target: builds and runs the Docker container"
	@echo "  $(WHEEL_FILE) - Checks for the wheel file; builds it using UV if not found"
	@echo "  $(MODEL_FILE) - Checks for the trained model; trains it if not found"
	@echo "  build     - Builds the Docker image (requires wheel and model)"
	@echo "  run       - Runs the Docker container on port $(PORT)"
	@echo "  clean     - Removes generated files (wheel and model)"
	@echo "  help      - Displays this help message"

# Check if the wheel exists, if not build it with UV
$(WHEEL_FILE):
	@echo "Checking for wheel file..."
	@if [ ! -f "$(WHEEL_FILE)" ]; then \
		echo "Wheel file not found. Building using UV..."; \
		uv build; \
	fi

# Check if the trained model exists, if not train it
$(MODEL_FILE):
	@echo "Checking for trained model..."
	@if [ ! -f "$(MODEL_FILE)" ]; then \
		echo "Model file not found. Training the model..."; \
		python src/slanggen/main.py; \
	fi

# Build the Docker image
build: $(WHEEL_FILE) $(MODEL_FILE)
	@echo "Building Docker image..."
	docker build -t $(DOCKER_IMAGE) .

# Run the Docker container
run: build
	@echo "Running Docker container on port $(PORT)..."
	docker run --rm -it -p $(PORT):8080 $(DOCKER_IMAGE)

# Clean up temporary files
clean:
	@echo "Cleaning up..."
	rm -f $(WHEEL_FILE)
	rm -f $(MODEL_FILE)
	@echo "Clean up complete."

# Start an interactive session inside the Docker image
interactive: build
	@echo "Starting an interactive session in the Docker image..."
	docker run --rm -it $(DOCKER_IMAGE) /bin/bash	
