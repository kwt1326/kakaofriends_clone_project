#!/bin/bash

RUN_PORT=$1
IMAGE_NAME="kwt1326/kakaofriends_clone_django_api"

function docker_build() {
  docker build -t $IMAGE_NAME .
}

function docker_run() {
  docker run \
  -e RUN_PORT=$RUN_PORT \
  --rm -d -p $RUN_PORT:$RUN_PORT \
  --name "project-server" $IMAGE_NAME
}

docker_build

docker_run