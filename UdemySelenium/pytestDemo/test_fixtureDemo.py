import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo2(self):
         print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo3(self):
        print("i will execute steps in fixtureDemo method")

    def test_fixtureDemo4(self):
        print("i will execute steps in fixtureDemo method")

