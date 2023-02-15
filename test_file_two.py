import pytest


def test_mySecondFile():
   a = 5
   b = 11
   assert a + b == 16 , "The function is true"

@pytest.mark.xfail
def test_myThirdFile():
   a = 5
   b = 10
   assert a + b == 16 , "The function is false"



def test_dummyTest():
   print("To check the fixture I am used")

