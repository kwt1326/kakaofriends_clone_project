#!/bin/sh

ls -al
mkdir ./env
gpg --quiet --batch --yes --decrypt --passphrase="$ENV_DECRYPE_PW" \
--output ./env/env.json env.json.gpg