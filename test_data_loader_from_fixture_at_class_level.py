import pytest


@pytest.mark.usefixtures("myData")
class TestExample:

    def test_fixtureTest1(self):
        print("Testing a fixture fixtureTest1")


    def test_fixtureTest2(self, myData):
        print("Testing a fixture fixtureTest2")
        print(myData)



    def test_fixtureTest3(self):
        print("Testing a fixture fixtureTest3")

