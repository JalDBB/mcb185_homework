import math


def quadratic_formula(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return []  # No real roots for a negative discriminant

    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)

    if root1 == root2:
        return [root1]
    else:
        return [root1, root2]


set1 = (1, -3, 2)
set2 = (1, 2, 1)
set3 = (2, -5, 2)

print(quadratic_formula(1,-3,2))
print(quadratic_formula(1,2,1))