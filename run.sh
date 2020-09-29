#/usr/bin/env bash
export PATH="/root/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
cd /var/www/html/fpl-statto && python3 /var/www/html/fpl-statto/statto.py