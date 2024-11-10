build:
	docker build -t fastapi-app:latest .
	docker run --p 8000:8000 fastapi-app:latest
	@echo "running on http://localhost:8000"


interactive:
	@echo "Entering container interactively"
	docker run -it fastapi-app:latest /bin/sh

local-setup:
	python -m venv .venv && pip install -e 
	
