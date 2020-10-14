import pytest

@pytest.fixture(scope="class")
def setup():
    print("i will be executing first")
    yield
    print("i will be executed last")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return["Marko","Poje","google.si"] #tuple


@pytest.fixture(params=[("chrome", "Marko", "Poje"),("Firefox","krneki"),("Edge","Opera")])
def crossBrowser(request):
    return request.param
