# Variables
IMAGE_NAME := test-demo
IMAGE_TAG := latest
PORT := 8000

# Colors
RED := \033[0;31m
GREEN := \033[0;32m
YELLOW := \033[1;33m
NC := \033[0m

# Docker image ID file to track builds
DOCKER_ID_FILE := .docker_image_id

# Phony targets
.PHONY: all build run train check-wheel clean test test-docker interactive help

# Default target
all: help

# Build Docker image if necessary
$(DOCKER_ID_FILE): Dockerfile $(wildcard src/**/*) $(wildcard requirements*.txt)
	@echo "$(YELLOW)Building $(IMAGE_NAME):$(IMAGE_TAG)$(NC)"
	@docker build -t $(IMAGE_NAME):$(IMAGE_TAG) .
	@docker inspect -f '{{.Id}}' $(IMAGE_NAME):$(IMAGE_TAG) > $(DOCKER_ID_FILE)
	@echo "$(GREEN)Build complete!$(NC)"

build: $(DOCKER_ID_FILE)

# Run Docker container
run: $(DOCKER_ID_FILE)
	@echo "$(YELLOW)Starting container $(IMAGE_NAME):$(IMAGE_TAG)...$(NC)"
	@docker stop $(IMAGE_NAME) 2>/dev/null || true
	@docker rm $(IMAGE_NAME) 2>/dev/null || true
	@echo "$(GREEN)Service running on http://localhost:$(PORT)$(NC)"
	@docker run -d -p $(PORT):$(PORT) --name $(IMAGE_NAME) $(IMAGE_NAME):$(IMAGE_TAG)

interactive: $(DOCKER_ID_FILE)
	@echo "$(YELLOW)Entering interactive shell...$(NC)"
	@docker run -it --rm \
		--entrypoint /bin/bash \
		$(IMAGE_NAME):$(IMAGE_TAG)

clean:
	@echo "$(YELLOW)Cleaning up...$(NC)"
	-docker stop $(IMAGE_NAME) 2>/dev/null || true
	-docker rm $(IMAGE_NAME) 2>/dev/null || true
	-docker rmi $(IMAGE_NAME):$(IMAGE_TAG) 2>/dev/null || true
	@rm -f $(DOCKER_ID_FILE)
	@echo "$(GREEN)Cleanup complete!$(NC)"

test: $(DOCKER_ID_FILE)
	@echo "$(YELLOW)Running unit and API tests...$(NC)"
	pytest -v -m "api or unit or hypothesis"
	pytest --cov=src -m "api or unit or hypothesis"
	@echo "$(GREEN)Tests complete!$(NC)"

test-docker: run
	@echo "$(YELLOW)Running integration tests...$(NC)"
	pytest -v -m integration
	pytest --cov=src -m integration
	@echo "$(GREEN)Integration tests complete!$(NC)"

help:
	@echo "Available targets:"
	@echo "  build        - Build Docker image if necessary"
	@echo "  run          - Run Docker container"
	@echo "  interactive  - Start interactive shell in container"
	@echo "  clean        - Remove container, image, and build artifacts"
	@echo "  test         - Run unit and API tests"
	@echo "  test-docker  - Run integration tests"
	@echo "  help         - Show this help message"
