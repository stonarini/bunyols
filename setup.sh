#!/bin/sh

git config --local core.hooksPath .githooks/

python3 -m venv venv

source ./venv/bin/activate
