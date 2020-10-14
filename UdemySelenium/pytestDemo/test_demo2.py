import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram2():
    msg = "hello"
    assert msg == "hello", "test failed because condition is"

def test_secondProgram2():
    a = 4
    b = 6
    assert a + b ==10, "addition do not match"

def test_CreditCard():
    a = 4
    b = 6
    assert a + b == 10, "addition do not match"

@pytest.fixture()
def setup():
    print("i will be executing first")

def test_fixtureDemo(setup):
    print("i will execute steps in fixtureDemo method")

#run specific py file: pytest test_demo2.py
#run only test which contains word: pytest -k CreditCard -v -s
#run smoke tests pytest -m smoke -v -s
