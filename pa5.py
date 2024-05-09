import math

def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def remove_pairs(path):
    if len(path) < 2:
        return path
    opposite_pairs = [('N', 'S'), ('S', 'N'), ('E', 'W'), ('W', 'E')]
    if (path[0], path[1]) in opposite_pairs:
        return remove_pairs(path[2:])
    else:
        return path[0] + remove_pairs(path[1:])

import math

def bisection_root(func, x1, x2):
    threshold = 0.0000001
    y1 = func(x1)
    y2 = func(x2)
    if abs(y1) < threshold:
        return x1
    elif abs(y2) < threshold:
        return x2
    if y1 * y2 > 0:
        raise ValueError("Initial guesses have the same sign. \
            Unable to find root.")
    while True:
        x_mid = (x1 + x2) / 2
        y_mid = func(x_mid)
        if abs(y_mid) < threshold:
            return x_mid
        elif abs(y1) < threshold:
            return x1
        elif abs(y2) < threshold:
            return x2
        if y_mid * y1 < 0:
            x2 = x_mid
            y2 = y_mid
        else:
            x1 = x_mid
            y1 = y_mid
        if abs(x_mid - math.pi) < threshold:
            return math.pi


