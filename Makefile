CURRENT_DIR := $(shell pwd)
VIRTUALENV_DIR = $(CURRENT_DIR)/venv

PIP = $(VIRTUALENV_DIR)/bin/pip
PYTHON = $(VIRTUALENV_DIR)/bin/python


help: _help_

_help_:
	@echo make deps - install all project requirments
	@echo make run - start the project server
	@echo make deploy - start server with prod config
	@echo make test - run tests 

deps:
	@if ! [ -d $(VIRTUALENV_DIR) ]; \
		then \
	 	echo 'Creating virtual environment.'; \
	  	virtualenv venv -p python3; \
	fi

	@echo "Installing packages from requirements/common"
	@$(PIP) install -r requirements/common

run:
	@ln -sf configs/dev.py ./config.py

	$(PYTHON) manage.py runserver


deploy: 
	@echo 'Hypothetically here may be script for starting server with prod config'


test:
	$(VIRTUALENV_DIR)/bin/pytest