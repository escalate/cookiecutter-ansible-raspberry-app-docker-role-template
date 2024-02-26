SHELL = /bin/bash
.SHELLFLAGS = -e -o pipefail -c

.PHONY: test
test: clean
	cookiecutter . \
	--output-dir=test/ \
	--replay \
	--replay-file cookiecutter-ansible-raspberry-app-docker-role-template.json \
	--keep-project-on-failure \
	--verbose

.PHONY: clean
clean:
	rm --recursive --force test/
