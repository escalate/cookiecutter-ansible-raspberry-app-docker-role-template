SHELL = /bin/bash -eo pipefail

.PHONY: lint
lint:
	ec
	flake8 hooks/

.PHONY: version
version:
	ec --version
	flake8 --version
