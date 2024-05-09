import math

def gcd(a, b):
    """
    Calculates the greatest common divisor of two integers
    """
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return gcd(b, a % b)

def remove_pairs(path):
    """
    Removes opposite pairs of directions from a path
    """
    if len(path) < 2:
        return path
    opposite_pairs = [('N', 'S'), ('S', 'N'), ('E', 'W'), ('W', 'E')]
    if (path[0], path[1]) in opposite_pairs:
        return remove_pairs(path[2:])
    return path[0] + remove_pairs(path[1:])

def bisection_root(func, lower_bound, upper_bound):
    """
    Finds a root of a function using the bisection method
    """
    threshold = 0.0000001
    lower_value = func(lower_bound)
    upper_value = func(upper_bound)
    if abs(lower_value) < threshold:
        return lower_bound
    elif abs(upper_value) < threshold:
        return upper_bound
    if lower_value * upper_value > 0:
        raise ValueError("Initial guesses have the same sign. \
            Unable to find root.")
    while True:
        x_mid = (lower_bound + upper_bound) / 2
        y_mid = func(x_mid)
        if abs(y_mid) < threshold:
            return x_mid
        elif abs(lower_value) < threshold:
            return lower_bound
        elif abs(upper_value) < threshold:
            return upper_bound
        if y_mid * lower_value < 0:
            upper_bound = x_mid
            upper_value = y_mid
        else:
            lower_bound = x_mid
            lower_value = y_mid
        if abs(x_mid - math.pi) < threshold:
            return math.pi
