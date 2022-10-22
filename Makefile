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

.PHONY: train
train:
	python train.py

.PHONY: run-app
run-app:
	streamlit run app.py

.PHONY: all
all:
	make train
	make run-app


