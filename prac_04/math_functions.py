def odd(number):
    """Return True if absolute of number is odd, False otherwise."""
    number = abs(number)   # abs(number) makes the number positive
    if number % 2 == 1:
        return True
    else:
        return False

    # return abs(number) % 2 == 1

def square_of(number):
    """Return the value of number to the power of 2."""
    return number ** 2

def power_of(base, index):
    """Return the value of base to the power of index."""
    return base ** index

def integer_divide(number, divisor):
    """Return the quotient of the division."""
    return number // divisor

def equal(rhs, lhs):
    """Return True if the numerical value of rhs equals numerical value of lhs."""
    are_numeric = str(rhs).isnumeric() and str(lhs).isnumeric()   # if both strings are numbers
    if are_numeric:
        return float(rhs) == float(lhs)     # check their float values
    else:
        return False

    # return are_numeric and float(rhs) == float(lhs)



