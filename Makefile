DOCKER_REPO=cdlm/weather-network-forecast-scraper

.PHONY: clean-pyc

build-function: clean-pyc  copy-src 

build-docker:
	docker build --tag $(DOCKER_REPO) .  

copy-src:
	rm -rf azure-function/src
	cp -r src azure-function/
	rm azure-function/requirements.txt
	cp requirements.txt azure-function/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -rf {} +