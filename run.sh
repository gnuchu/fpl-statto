#/usr/bin/env bash
export PATH="/root/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
cd /var/www/html/stats&& python3 /var/www/html/stats/statto.py
