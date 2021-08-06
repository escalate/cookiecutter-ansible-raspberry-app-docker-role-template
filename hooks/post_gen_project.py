#!/usr/bin/env python

import os

app_config = "{{ cookiecutter.app_config_yaml | lower }}"
app_backup_job = "{{ cookiecutter.app_backup_job | lower }}"

if app_config == "false":
    os.remove("./templates/{{ cookiecutter.app_name_slug }}.yml.j2")

if app_backup_job == "false":
    os.remove("./templates/backup-{{ cookiecutter.app_name_slug }}.sh.j2")
