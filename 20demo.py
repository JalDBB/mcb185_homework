print ("hello, again") # greeting
"""
This is a 
multi-line
comment
"""
print('hello, again') # greeting
print(1.5e-2)

Import math

print('hello, again')
print(1.5e-2)
print(1 + 1)
print(2 ** 3)
print(pow(2, 3))
print(math.pow(2, 3))
print(2 ** 0.5)
print(math.sqrt(2))
print(math.log(2))

print(0.1 * 1)
print(0.1 * 3)

a = 3                       # side of triangle
b = 4                       # side of triangle
c = math.sqrt(a**2 + b**2)  # hypotenuse
print(c)
print(type(a), type(b), type(c))
print(type(a), type(b), type(c), sep=', ')
def greeting():
    print('hello yourself')
def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c
x = pythagoras(3, 4)
print(x)
def pythagoras(a, b):
    return math.sqrt(a**2 + b**2)

print(pythagoras(3, 4))
print(pythagoras(1, 1))
def pythagoras(a, b):
    assert(a > 0)
    assert(b > 0)
    return math.sqrt(a**2 + b**2)

print(pythagoras(-1, 1))
import sys

def pythagoras(a, b):
    if a <= 0: sys.exit('error: a must be greater than 0')
    if b <= 0: sys.exit('error: b must be greater than 0')
    return math.sqrt(a**2 + b**2)
def midpoint(x1, y1, x2, y2):
    # insert stuff here
    return mx, my