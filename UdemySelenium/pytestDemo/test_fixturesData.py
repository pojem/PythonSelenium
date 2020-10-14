import pytest

from pytestDemo.baseClass import BaseClass

@pytest.mark.usefixtures("dataload")

class TestExample2(BaseClass):

    def test_editprofile(self,dataload):
        print("i will execute steps in fixtureDemo method")
        a = (dataload[1])
        b = (dataload[0])
        print(a+b)
        log = self.getLogger()  # LOG PRINT
        log.info(a+b)


