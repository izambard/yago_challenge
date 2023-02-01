# Specific project settings
APP_NAME?=yago
DOCKER_FILE?=deployment/Dockerfile

# Misc
INPUT?='coco'
TAG_NAME?=latest

REST_PORT=80
HOST=0.0.0.0
WEB_CONCURRENCY=1
ENV_FILE=docker.env

API_CMD=conda run --no-capture-output -n $(APP_NAME) python -m uvicorn service.api:app --port $(REST_PORT) --host $(HOST) --env-file $(ENV_FILE)

help:
	@cat Makefile

echo:
	# Echoing an input
	echo $(INPUT)

build:
	docker build -t $(APP_NAME) -f $(DOCKER_FILE) .	

run_api:
	docker run -p $(REST_PORT):$(REST_PORT) -e WEB_CONCURRENCY=$(WEB_CONCURRENCY) --name $(APP_NAME) $(APP_NAME) $(API_CMD)

rm:
	# Removing docker container
	docker rm $(APP_NAME)

