import pytest


@pytest.fixture
def globalFixture():
    print("I am a global fixture")



# To learn about data load
@pytest.fixture
def myData():
    return("This","is","data","load","test")





#If there are multiple values that we need to send through the data then we use the param
# request is the instance through which we pass the fixture value
@pytest.fixture(params=[("chrome","Arvindh"), ("Firefox", "Rider"), ("Safari", "Tester")])
def crossBrowser(request):
    return request.param