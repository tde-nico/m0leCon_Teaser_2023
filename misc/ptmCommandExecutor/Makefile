DOCKER = sudo docker

IMAGE = pwner

init:
	pwninit

pwn:
	$(DOCKER) run -it --rm -v "$(pwd):/chal" $(IMAGE) /bin/bash

build:
	$(DOCKER) build -t $(IMAGE) .
