# Variables
IMAGE_NAME := test-demo
IMAGE_TAG := latest
PORT := 8000

# Colors
RED := \033[0;31m
GREEN := \033[0;32m
NC := \033[0m # No Color

# Phony targets to prevent conflicts with files of the same name
.PHONY: all build run train check-wheel

# Default target
all: build

# Build Docker image, depends on .whl file
build:
	@echo "$(YELLOW) building $(IMAGE_NAME):$(IMAGE_TAG)"
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	@echo "$(GREEN)Build complete!$(NC)"

# Run Docker container
run:
	@echo "$(YELLOW)Starting container $(IMAGE_NAME):$(IMAGE_TAG)...$(NC)"
	@docker stop $(IMAGE_NAME) 2>/dev/null || true
	@docker rm $(IMAGE_NAME) 2>/dev/null || true
	@echo "$(GREEN)Service running on http://localhost:$(PORT)$(NC)"
	docker run -d -t -p $(PORT):$(PORT) --name $(IMAGE_NAME) $(IMAGE_NAME):$(IMAGE_TAG)

interactive: build
	@echo "$(YELLOW)Entering interactive shell...$(NC)"
	docker run -it --rm \
		--entrypoint /bin/bash \
		$(IMAGE_NAME):$(IMAGE_TAG)

clean:
	@echo "$(YELLOW)Cleaning up...$(NC)"
	-docker stop $(IMAGE_NAME) 2>/dev/null || true
	-docker rm $(IMAGE_NAME) 2>/dev/null || true
	-docker rmi $(IMAGE_NAME):$(IMAGE_TAG) 2>/dev/null || true
	@echo "$(GREEN)Cleanup complete!$(NC)"

test:
	pytest -v -m "api or unit or hypothesis"
	pytest --cov=src -m "api or unit or hypothesis"

test-docker:
	pytest -v -m integration
	pytest --cov=src -m integration
