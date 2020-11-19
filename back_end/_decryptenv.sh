#!/bin/sh

mkdir $HOME/env
gpg --quiet --batch --yes --decrypt --passphrase="$ENV_DECRYPE_PW" \
--output $HOME/env/env.json $HOME/env.json.gpg