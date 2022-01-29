import json
import logging
import os

import subprocess
import paramiko
from setup import *

host_name = pytest.config_file.get("system", "host_url")
host_user = pytest.config_file.get("system", "host_user")
host_pass = pytest.config_file.get("system", "host_pass")


def connect_to_host_with_ssh():
    response = os.system("ping -c 1 " + host_name)
    # and then check the response...
    if response == 0:
        logging.info(host_name + ", 'is up!'")
    else:
        logging.info(host_name + ", 'is down!'")
        logging.error("ping response => " + response)
        pytest.fail("host " + host_name + " is down , cannot ping it :-(")

    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=host_name, port="22", username=host_user, password=host_pass, timeout=10)
    return ssh_client


def run_command_return_string(ssh_client, cmd):
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    lines = stdout.readlines()
    return str(lines)


def run_command(ssh_client, cmd):
    stdin, stdout, stderr = ssh_client.exec_command(cmd)


def run_command_return_json(ssh_client, cmd):
    stdin, stdout, stderr = ssh_client.exec_command(cmd)
    lines = stdout.readlines()
    dict_lines = json.loads(lines[0])
    return dict_lines


def run_cmd_locally(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        print(line)