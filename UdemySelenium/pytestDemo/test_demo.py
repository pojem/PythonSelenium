#any pytest file should start with test_ or and and with _test
#any test method names should start with test
#any code should be wrapped in method only
#method name should have sense
# - k stands for method names execution, -s logs in output, v stands for more info
#you can run specific file with pytest <filename>
#you can mark (tag) @pytest.mark.smoke tests and then run with -m (smoke, regression testing...)
#skip particular test case with mark @pytest.mark.skip
#fixtures are used for setup and tear down methods for test cases - conftest file to generalize fixtures
#fixture and make it available to all test cases
# datadriven and parametrization can be done with return statements in tuple format
#when you define fixtrure scope to class only it will run once before class is initiated and at the end

import pytest
from pytestDemo.baseClass import BaseClass


@pytest.mark.smoke
def test_firstProgram(setup):
    print("hello pytest")

#if you want to run all tests in directory pytest -v -s

@pytest.mark.xfail #running but not reporting
def test_secondProgram():
    print("hello test2")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])

#to generate report run command : pytest --html=report.html
# to install pytest-html run command "pip install pytest-html"