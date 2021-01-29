from pytest import approx


def test_float_without_approx():
    """This test will fail"""
    assert (0.1+0.2) == 0.3


def test_float_with_approx():
    """This test will not fail"""
    assert (0.1+0.2) == approx(0.3)
