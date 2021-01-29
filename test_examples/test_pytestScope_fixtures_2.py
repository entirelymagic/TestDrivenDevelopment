import pytest


@pytest.fixture(scope="module", autouse=True)
def setupSession():
    print("\nSetup Module2")


@pytest.fixture(scope="class", autouse=True)
def setupModule():
    print("\nSetup Class2")


@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function2")


class TestClass:
    def test_it1(self):
        print("Executing test1")
        assert True

    def test_it2(self):
        print("Executing test2")
        assert True
