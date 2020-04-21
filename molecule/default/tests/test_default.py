"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["git"])
def test_packages(host, pkg):
    """Test that the expected packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("f", ["/opt/ServerSetup", "/opt/ServerSetup/serversetup.sh"])
def test_files(host, f):
    """Test that the expected files and directories are present."""
    assert host.file(f).exists
