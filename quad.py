import math

def quadratic_formula(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: {root1} and {root2}"