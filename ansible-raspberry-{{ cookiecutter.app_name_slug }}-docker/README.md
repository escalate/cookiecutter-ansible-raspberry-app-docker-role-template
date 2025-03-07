[![Test](https://github.com/{{ cookiecutter.author_github_user_name }}/ansible-raspberry-{{ cookiecutter.app_name_slug }}-docker/actions/workflows/test.yml/badge.svg?branch=master&event=push)](https://github.com/{{ cookiecutter.author_github_user_name }}/ansible-raspberry-{{ cookiecutter.app_name_slug }}-docker/actions/workflows/test.yml)

# Ansible Role: Raspberry - {{ cookiecutter.app_name }} (Docker)

An Ansible role that manages [{{ cookiecutter.app_name }}]({{ cookiecutter.app_website }}) Docker container with systemd on Raspberry Pi OS (Debian Bookworm).

## Role Variables

Please see [defaults/main.yml](https://github.com/{{ cookiecutter.author_github_user_name }}/ansible-raspberry-{{ cookiecutter.app_name_slug }}-docker/blob/master/defaults/main.yml) for a complete list of variables that can be overridden.

## Dependencies

This role relies on the following dependencies:

- Roles: [requirements.yml](https://github.com/{{ cookiecutter.author_github_user_name }}/ansible-raspberry-{{ cookiecutter.app_name_slug }}-docker/blob/master/requirements.yml)
- Collections: [requirements.yml](https://github.com/{{ cookiecutter.author_github_user_name }}/ansible-raspberry-{{ cookiecutter.app_name_slug }}-docker/blob/master/requirements.yml)

## Installation

```
$ ansible-galaxy role install {{ cookiecutter.author_galaxy_namespace }}.{{ cookiecutter.app_name_ansible_var }}
```

## Example Playbook

```
- hosts: all
  roles:
    - role: {{ cookiecutter.author_galaxy_namespace }}.{{ cookiecutter.app_name_ansible_var }}
      tags: {{ cookiecutter.app_name_ansible_tag }}
```

## License

MIT
