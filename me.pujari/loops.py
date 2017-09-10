# Simple  Fibonacci with while loop

print("Usual way")

f = 200
x = 0
y = 1
t = 0

while x < f:
    print(x)
    t = x
    x = y
    y = t + y

# This can also be written as follows in python

print("Python way")

f = 200
x = 0
y = 1

while x < f:
    print(x)
    x, y = y, x + y
