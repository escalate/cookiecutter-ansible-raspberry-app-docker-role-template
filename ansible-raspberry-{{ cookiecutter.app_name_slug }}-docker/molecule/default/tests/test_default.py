"""Role testing files using testinfra"""


def test_config_directory(host):
    """Check config directory"""
    f = host.file("/etc/{{ cookiecutter.app_name_slug }}")
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_data_directory(host):
    """Check data directory"""
    d = host.file("/var/lib/{{ cookiecutter.app_name_slug }}")
    assert d.is_directory
    assert d.user == "{{ cookiecutter.app_name_slug }}"
    assert d.group == "root"
    assert d.mode == 0o775


{% if cookiecutter.app_backup_job | lower == "true" -%}
def test_backup_directory(host):
    """Check backup directory"""
    b = host.file("/var/backups/{{ cookiecutter.app_name_slug }}")
    assert b.is_directory
    assert b.user == "{{ cookiecutter.app_name_slug }}"
    assert b.group == "root"
    assert b.mode == 0o775


{% endif -%}
{% if cookiecutter.app_config_yaml | lower == "true" -%}
def test_{{ cookiecutter.app_name_ansible_var }}_config(host):
    """Check {{ cookiecutter.app_name }} config file"""
    f = host.file("/etc/{{ cookiecutter.app_name_slug }}/{{ cookiecutter.app_name_slug }}.yml")
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"

    # TODO
    config = (
        ""
    )
    assert config in f.content_string


{% endif -%}
def test_{{ cookiecutter.app_name_ansible_var }}_service(host):
    """Check {{ cookiecutter.app_name }} service"""
    s = host.service("{{ cookiecutter.app_name_slug }}")
    assert s.is_running
    assert s.is_enabled


def test_{{ cookiecutter.app_name_ansible_var }}_docker_container(host):
    """Check {{ cookiecutter.app_name }} docker container"""
    d = host.docker("{{ cookiecutter.app_name_slug }}.service").inspect()
    assert d["HostConfig"]["Memory"] == 1073741824
    assert d["Config"]["Image"] == "{{ cookiecutter.app_docker_image }}:latest"
    assert d["Config"]["Labels"]["maintainer"] == "me@example.com"
    # TODO
    assert "APP_TEST_ENV=true" in d["Config"]["Env"]
    assert "internal" in d["NetworkSettings"]["Networks"]
    assert \
        "{{ cookiecutter.app_name_slug }}" in d["NetworkSettings"]["Networks"]["internal"]["Aliases"]
{%- if cookiecutter.app_backup_job | lower == "true" %}


def test_backup(host):
    """Check if the backup runs successfully"""
    cmd = host.run("/usr/local/bin/backup-{{ cookiecutter.app_name_slug }}.sh")
    assert cmd.succeeded


def test_backup_cron_job(host):
    """Check backup cron job"""
    f = host.file("/var/spool/cron/crontabs/root")
    assert "/usr/local/bin/backup-{{ cookiecutter.app_name_slug }}.sh" in f.content_string


def test_restore(host):
    """Check if the restore runs successfully"""
    cmd = host.run("/usr/local/bin/restore-{{ cookiecutter.app_name_slug }}.sh")
    assert cmd.succeeded
{%- endif -%}
