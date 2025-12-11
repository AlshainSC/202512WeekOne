# Calculator operations module
# Contains basic arithmetic functions for the calculator application

SUPPORTED_OPERATIONS = ["add", "subtract", "multiply", "divide"]


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b. Returns None if b is zero."""
    if b == 0:
        return None
    return a / b
