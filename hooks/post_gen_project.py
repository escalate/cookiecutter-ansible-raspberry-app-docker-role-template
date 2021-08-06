#!/usr/bin/env python

import os

author_funding_url = "{{ cookiecutter.author_funding_url | trim }}"
app_config = "{{ cookiecutter.app_config_yaml | lower }}"
app_backup_job = "{{ cookiecutter.app_backup_job | lower }}"

if len(author_funding_url) == 0:
    os.remove("./.github/FUNDING.yml")

if app_config == "false":
    os.remove("./templates/{{ cookiecutter.app_name_slug }}.yml.j2")

if app_backup_job == "false":
    os.remove("./templates/backup-{{ cookiecutter.app_name_slug }}.sh.j2")
