# Cookiecutter - Ansible role template for Docker applications on Raspberry Pi OS

An Cookiecutter Ansible role template for Docker applications on Raspberry Pi OS.

## How to use?

```
$ cookiecutter https://github.com/escalate/cookiecutter-ansible-raspberry-app-docker-role-template.git
```

## What options are available for generation?

| Option                  | Default                          | Description |
| ----------------------- | -------------------------------- | ----------- |
| author_full_name        | Felix Börner                     | Name of the Ansible role author |
| author_galaxy_namespace | escalate                         | Galaxy namespace of Ansible role author |
| author_github_user_name | escalate                         | Github username of Ansible role author |
| author_funding_url      | https://paypal.me/felixboerner   | Funding URL of Ansible role author |
| app_name                | Grafana                          | Application name (including whitespaces) |
| app_name_slug           | grafana                          | Lowercase and whitespace-less version of application name |
| app_name_ansible_var    | grafana                          | Lowercase and underscore version of application name |
| app_name_ansible_tag    | grafana                          | Lowercase, letter and digits version of application name |
| app_user_uid            | 10000                            | UID of application user (must be above 10000) |
| app_docker_image        | grafana/grafana                  | Docker Hub image name |
| app_port                | 3000                             | Published application port |
| app_website             | https://grafana.com/oss/grafana/ | Public website of application |
| app_config_yaml         | true                             | Switch to generate YAML configuration file for application [true, false] (str) |
| app_backup_job          | true                             | Switch to generate backup job for application [true, false] (str) |

## License

MIT
