#!/bin/sh

git config --local core.hooksPath .githooks/

python -m venv venv

source ./venv/bin/activate
