SHELL := /bin/bash

-include Makefile.base

BRANCH ?= master
LANGUAGE ?=
DOMAIN != github.com

BOILERPLATE_REPO_PATH = git@github.com:Filip-231/Boilerplate.git
BOILERPLATE_REPO_SSH = git@$(DOMAIN):$(BOILERPLATE_REPO_PATH)


.PHONY: update
update::
	@echo "Updating Makefiles"
	git archive --remote="$(BOILERPLATE_REPO_PATH)" "$(BRANCH)" cicd/Makefile.cicd templates/Makefile.common | \
		tar --extract --overwrite --strip-components=1
	git archive --remote="$(BOILERPLATE_REPO_PATH)" "$(BRANCH)" "templates/$(LANGUAGE)/Makefile.base" | \
		tar --extract --overwrite --strip-components=2