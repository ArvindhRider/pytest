import pytest


@pytest.fixture
def globalFixture():
    print("I am a global fixture")



# To learn about data load
@pytest.fixture
def myData():
    return("This","is","data","load","test")

