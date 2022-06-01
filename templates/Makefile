SHELL := /bin/bash

-include Makefile.base

BRANCH ?= master
LANGUAGE ?= python
DOMAIN ?= github.com

BOILERPLATE_REPO_PATH = git@github.com:Filip-231/Boilerplate.git
BOILERPLATE_REPO_SSH = git@$(DOMAIN):$(BOILERPLATE_REPO_PATH)

_VENV=.venv
_VENV_ACTIVATE = $(_VENV)/bin/activate

.PHONY: update
update::
	@echo "Updating Makefiles"
	git archive --remote="$(BOILERPLATE_REPO_PATH)" "$(BRANCH)" cicd/Makefile.cicd templates/Makefile.common | \
		tar --extract --overwrite --strip-components=1
	git archive --remote="$(BOILERPLATE_REPO_PATH)" "$(BRANCH)" "templates/$(LANGUAGE)/Makefile.base" | \
		tar --extract --overwrite --strip-components=2



.PHONY: test
test::
	@echo "Updating Makefiles"

.PHONY: venv
venv: $(_VENV_ACTIVATE) ## (create/recreate the python virtual environment)


$(_VENV_ACTIVATE):
	python -m venv --clear "$(_VENV)" && \
		. $@ && \
		pip install --upgrade pip
	touch $@