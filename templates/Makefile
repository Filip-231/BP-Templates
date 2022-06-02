SHELL := /bin/bash

-include Makefile.base


BRANCH ?= master
LANGUAGE ?= python
DOMAIN ?= github.com

BOILERPLATE_REPO_PATH = git@github.com:Filip-231/Boilerplate.git
BOILERPLATE_REPO_SSH = git@$(DOMAIN):$(BOILERPLATE_REPO_PATH)

_VENV=.venv
_VENV_ACTIVATE = $(_VENV)/bin/activate
_CURRENT_DIR_NAME = $(shell basename $${PWD})
#.PHONY: update
#update::
#	@echo "Updating Makefiles"
#	git archive --remote="$(BOILERPLATE_REPO_PATH)" "$(BRANCH)" cicd/Makefile.cicd templates/Makefile.common | \
#		tar --extract --overwrite --strip-components=1
#	git archive --remote="$(BOILERPLATE_REPO_PATH)" "$(BRANCH)" "templates/$(LANGUAGE)/Makefile.base" | \
#		tar --extract --overwrite --strip-components=2



.PHONY: test
test::
	@echo "Updating Makefiles"
	@echo $(shell basename $${PWD})


#.PHONY: init
#init: pre-install venv
#	$(info Initialising directory from template...)
#	$(info This will overwrite the contents of your current working directory. Are you sure you wish to continue? [y/n])
#	@read response; \
#	if [ $${response} = "y" ]; then \
#	echo "Initialising..."; \
#	find . -depth -path "./.git*" -prune -o \( \! -path "./Makefile*" \) \( \! -name "./.env" \) \
#		\( \! -path "./.venv*" \) -exec rm -rf {} \; 2> /dev/null; \
#	else \
#	echo "Aborting..."; \
#	exit 1; \
#	fi
#	. $(_VENV_ACTIVATE) && \
#		cruft create --output-dir=.. --directory=templates/django --overwrite-if-exists --checkout=$(BRANCH) \
#			--extra-context="{\"project_name\": \"$(_CURRENT_DIR_NAME)\"}" $(BOILERPLATE_REPO_PATH)
#
#
#.PHONY: pre-install
#pre-install: venv
#	. $(_VENV_ACTIVATE) && \
#		pip install $(if $(UPGRADE),--upgrade )commitizen cruft pre-commit && \
#			if [ -n "$(SKIP_PRE_COMMIT)" ]; then \
#			echo "SKIP_PRE_COMMIT detected; ignoring pre-commit setup..."; \
#			else \
#				if [ -n "$(UPGRADE)" ]; then \
#				pre-commit autoupdate --config=.pre-commit-config.yml; \
#				fi; \
#				pre-commit install --allow-missing-config --config=.pre-commit-config.yml --hook-type=pre-commit \
#					--hook-type=commit-msg; \
#			fi
#
#.PHONY: venv
#venv: $(_VENV_ACTIVATE)
#
#
#$(_VENV_ACTIVATE):
#	python -m venv --clear "$(_VENV)" && \
#		. $@ && \
#		pip install --upgrade pip
#	touch $@