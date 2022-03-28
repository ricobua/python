from numpy import random

x = random.randint(10)
y = random.randint(10)
res = input(str(x) + " * " + str(y) + " = ")

if int(res) == x*y:
    print("right")
else:
    print("wrong")
