import pytest


@pytest.fixture(params=[1, 2, 3])
def setup(request):
    retVal = request.param
    print(f"\nSetup! retval={retVal}")
    return retVal


def test1(setup):
    print(f"\nsetup = {setup}")
    assert True
