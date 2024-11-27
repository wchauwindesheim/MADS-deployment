build:
	@echo "building docker image"
	docker build -t fastapi-app:latest .

run:
	docker run -p 8000:8000 fastapi-app:latest
	@echo "running on http://localhost:8000"

interactive:
	@echo "Entering container interactively"
	docker run -it --entrypoint /bin/bash fastapi-app:latest
	
