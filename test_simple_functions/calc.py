def add(x, y):
    """Add function"""
    return x + y


def subtract(x, y):
    """subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ZeroDivisionError("Can not divide by zero")
    return x / y
