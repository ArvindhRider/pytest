import pytest


@pytest.mark.usefixtures("globalFixture")
class TestExample:

    def test_fixtureTest1(self):
        print("Testing a fixture fixtureTest1")


    def test_fixtureTest2(self):
        print("Testing a fixture fixtureTest2")



    def test_fixtureTest3(self):
        print("Testing a fixture fixtureTest3")

