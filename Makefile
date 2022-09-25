SHELL := /bin/bash
.SHELLFLAGS := -eu -o pipefail -c

API_KEY ?= AIzaSyDIWeB8PP2QLE-bhKrFwMK5vdCQwm1vQws

### Define development tasks ###
.PHONY: py-env
py-env:
	pipenv install --dev
	pipenv clean
	pipenv shell

.PHONY: get-data
get-data:
	python main.py ${API_KEY}

