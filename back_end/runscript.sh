#!/bin/bash

RUN_PORT=$1
IMAGE_NAME="kakaofriends_clone_project"

function docker_build() {
  docker build -t $IMAGE_NAME
}

function docker_run() {
  docker run \
  -e RUN_PORT=$RUN_PORT \
  -rm -d -p $RUN_PORT:$RUN_PORT \
  --name "$IMAGE_NAME-dev" $IMAGE_NAME
}

docker_build

docker_run