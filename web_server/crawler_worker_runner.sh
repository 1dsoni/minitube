#!/usr/bin/env bash
# to perform all the steps for running the project in a docker

./wait-for-it.sh -t 300 web_server:8000 -- echo crawler server is up

python3.8 manage.py start_crawl
