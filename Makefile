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