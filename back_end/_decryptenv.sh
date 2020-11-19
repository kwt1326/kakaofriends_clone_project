#!/bin/sh

mkdir $HOME/back_end/env
gpg --quiet --batch --yes --decrypt --passphrase="$ENV_DECRYPE_PW" \
--output $HOME/back_end/env/env.json ./back_end/env.json.gpg