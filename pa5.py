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

def bisection_root(func, lower_bound, upper_bound):
    threshold = 0.0000001
    lower_value = func(lower_bound)
    upper_value = func(upper_bound)
    
    if abs(lower_value) < threshold:
        return lower_bound
    elif abs(upper_value) < threshold:
        return upper_bound
    
    if lower_value * upper_value > 0:
        raise ValueError("Initial guesses have the same sign. Unable to find root.")
    
    while True:
        mid_point = (lower_bound + upper_bound) / 2
        mid_value = func(mid_point)
        
        if abs(mid_value) < threshold:
            return mid_point
        elif abs(lower_value) < threshold:
            return lower_bound
        elif abs(upper_value) < threshold:
            return upper_bound
        
        if mid_value * lower_value < 0:
            upper_bound = mid_point
            upper_value = mid_value
        else:
            lower_bound = mid_point
            lower_value = mid_value
        
        if abs(mid_point - math.pi) < threshold:
            return math.pi

