import pytest


@pytest.fixture()
def setup():
    print("I am a setup and I would before ")
    yield
    print("I run after tests")


def test_to_test_fixture(setup):
    print("Testing a fixture")

