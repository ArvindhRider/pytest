# Any pytest file should start with test_ or end with _test
# use pip 3 install pytest and after that
# Pytest method names should start with test
# And to run all the py tests just do py.test, bundle py.test -v
# Use py.test -v -s to get the log
# if two test methods are with the same name then the latter would override the previous
# if we need to run a specific test case then just mention that file name py.test filename -v -s
# test card name in pytest is the method name
# to run individual tests use py.test -k, where k stands for the method name execution -s for logs -v meta data
# py.test -k printing -v -s to run a particular test among many
# we use @pytest.mark nameofmark and give the name to mark and run the test case (need to import pytest here) this is similar to groups
# To run it py.test -m nameofmark -v -s
# to skip tests we can use @pytest.mark.skip
# just like protractor x in it block --> @pytest.mark.xfail to skip that test
# fixtures are nothing but before and after test kind of
# to write a fixture --> @pytest.fixture() it can be anywhere in the file
# .........Like after test in Java
# we do not separately need to write annotations here
# we can simply use
# "yield" statement
# so the any statement after yield will be executed after the test suite like after test........
# To make the fixture globally available we do create a file called conftest.py
# Use the exact name as mentioned
# instead of giving the fixtures seperately in all the test method we can
# create a class and use @pytest.mark.usefixtures("fixturename") to pass that fixture value
#  The class name should be always written with "Test" not in small words
# if we have a requirement where we need to run the fixture only before the class gets run and not everytime the methods are run
# 1) Go to the conftest.py file
# 2) under @pytest.fixture(scope="class")
# 3) we have given that the scope is only at the class level
# example clearing the browser cache before the browser is initialized
# basically data driven and parametrization can be done withh return statements
# when we pass multiple values we use params = [] inside the usefixtures and inside the method we use request instance
# @pytest.fixture(params=[("chrome","Arvindh"), ("Firefox", "Rider"), ("Safari", "Tester")])
# def crossBrowser(request):
#     return request.param   this is like obj.value
# Ultimately we have to get all these informations in a file so we use two things
# 1) addhandler and
# 2) file handler
# file handler has to ability to create a new file for the logs
# like
# logging.filehandler('logfile.log')
# this has to be passed to addhandler


import pytest
import test_fixuredemo



def test_my_method(globalFixture):
    print("This is a pytest trail")


@pytest.mark.run
def test_printing():
    print("I am a selected module test case")

def test_crossbrowsing(crossBrowser):
    print(crossBrowser)
    print(crossBrowser[1])




