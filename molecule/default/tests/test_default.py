import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    s = host.service('mongod')
    assert s.is_running


def test_socket(host):
    s = host.socket('tcp://127.0.0.1:27017')
    assert s.is_listening
