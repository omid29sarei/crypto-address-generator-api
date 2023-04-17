#! /usr/bin/make -f

.PHONY: help
help:
	@echo "Welcome to the Wallet Generator API"
	@echo "Command Available Are: "
	@echo "dev-mode"

.PHONY: dev-mode
dev-mode:
	python3 ./manage.py makemigrations
	python3 ./manage.py migrate
	python3 ./manage.py runserver

.PHONY: dev-docker
dev-docker:
	docker build --tag=wallet_generator -f ./docker/Dockerfile .
	docker run -p 127.0.0.1:8000:8000 wallet_generator

.PHONY: dev-test
dev-test:
	python3 ./manage.py test