"""Using pytest to run this testing."""


def isMultiple(value, mod):
    return (value % mod) == 0


def fizzBuzz(value):
    if isMultiple(value, 3):
        if isMultiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    elif isMultiple(value, 5):
        return "Buzz"
    return str(value)


def checkFizzBuzz(value, expected_ret_val):
    retValue = fizzBuzz(value)
    assert retValue == expected_ret_val


def test_returns1With1PassedIn():
    retVal = fizzBuzz(1)
    assert retVal == '1'


def test_returns2With2PassedIn():
    retVal = fizzBuzz(2)
    assert retVal == '2'


def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3, 'Fizz')


def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5, "Buzz")


def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6, 'Fizz')


def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10, 'Buzz')


def test_returnsFizzBuzzWith15PassedIn():
    checkFizzBuzz(15, "FizzBuzz")
