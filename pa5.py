def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0: # base case
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

def bisection_root(func, x1, x2):
    max_iterations = 1000
    if func(x1) * func(x2) > 0:
        raise ValueError("Initial guesses do not bracket the root.")
    
    for _ in range(max_iterations):
        x_mid = (x1 + x2) / 2
        y_mid = func(x_mid)
        
        if abs(y_mid) < 0.001:
            return x_mid
        if func(x1) * y_mid < 0:
            x2 = x_mid
        else:
            x1 = x_mid
    raise ValueError("Bisection method failed to converge.")

