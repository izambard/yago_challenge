# Specific project settings
APP_NAME?=yago
DOCKER_FILE?=deployment/Dockerfile

# Misc
INPUT?='coco'

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

AWS_CLI=aws
export AWS_DEFAULT_REGION=eu-west-1

# AWS connection settings - better being in env
TAG_NAME?=latest
AWS_ECR_SCOPE?=yago/
AWS_ECR_ROOT?=876999595319.dkr.ecr.$(AWS_DEFAULT_REGION).amazonaws.com/$(AWS_ECR_SCOPE)
AWS_ECR_PATH?=https://876999595319.dkr.ecr.$(AWS_DEFAULT_REGION).amazonaws.com
AWS_ECR_REST_IMAGE_ARN?="$(AWS_ECR_ROOT)$(APP_NAME):$(TAG_NAME)"

ecr_login:
	# Logging to AWS ECR
	$(AWS_CLI) ecr get-login-password --region eu-west-1 | docker login --username AWS --password-stdin $(AWS_ECR_PATH)

ecr_tag:
	# Tagging docker image before push to AWS ECR
	docker tag $(APP_NAME):$(TAG_NAME) $(AWS_ECR_ROOT)$(APP_NAME):$(TAG_NAME)

ecr_create_repo:
	$(AWS_CLI) ecr create-repository --repository-name $(AWS_ECR_SCOPE)$(APP_NAME)

ecr_push: ecr_tag ecr_login
	# Pushing docker image to AWS ECR
	docker push $(AWS_ECR_ROOT)$(APP_NAME):$(TAG_NAME)
