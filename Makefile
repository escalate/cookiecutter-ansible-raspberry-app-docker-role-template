SHELL = /bin/bash
.SHELLFLAGS = -e -o pipefail -c

.PHONY: lint
lint:
	ec
	flake8 hooks/

.PHONY: version
version:
	ec --version
	flake8 --version
