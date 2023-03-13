.DEFAULT_GOAL := default

# env
TAG=gspot-frontend:latest
NAME=gspot_production_frontend
PORT=3000

# commands
dev:
	- docker-compose up
build:
	- docker build -f Dockerfile.prod -t ${TAG} .
run:
	- docker run --name ${NAME} -d -p ${PORT}:3000 ${TAG}
default: dev