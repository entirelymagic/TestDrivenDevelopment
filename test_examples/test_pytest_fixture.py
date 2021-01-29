import pytest


@pytest.fixture()
def setup1():
    """
    - When the "yield" keyword is used the code after the Yield is executed after the fixture goes out of scope.
    - The "yield" keyword is replacement for the return keyword so any return values are also specified in the
    yield statement'
    """
    print("Setup1")
    yield
    print("Teardown setup1")


@pytest.fixture()
def setup2(request):
    """
    - With the addfinalizer method a teardown method is defined added via the request-context's addfinalizer method.
    - Multiple finalization functions can be specified.
    :param request:
    :return:
    """
    print("Setup2!")

    def teardown_a():
        print("Teardown A")

    def teardown_b():
        print("Teardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1):
    print("Executing test1!")
    assert True


def test2(setup2):
    print("Executing test2!")
    assert True
