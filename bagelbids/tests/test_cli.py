import pytest
from click.testing import CliRunner

from bagelbids.cli import bagel


@pytest.fixture
def runner():
    return CliRunner()


# TODO: remove this dummy test
def test_bids(bids_synthetic):
    assert bids_synthetic.is_dir()


def test_fails_if_no_arguments_provided(runner):
    result = runner.invoke(bagel)
    assert result.exit_code == 2
