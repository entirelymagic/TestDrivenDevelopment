from pytest import raises


def raisesValueException():
    raise ValueError


def not_raisesValueException():
    pass


def test_ValueError_exception1():
    """Test will pass as the function will raise ValueError"""
    with raises(ValueError):
        raisesValueException()


def test_ValueError_exception2():
    """Test will fail as the function will not raise ValueError"""
    with raises(ValueError):
        not_raisesValueException()

