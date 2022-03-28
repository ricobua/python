from numpy import random

x = random.randint(10) # random Zufall int integer
print("Die Zahl x ist dieses Mal: " + str(x))
y = random.randint(10)
print("Die Zahl y ist dieses Mal: " + str(y))


print(str(x) + " * " + str(y) + " = ")
input() # dear computer, please ask the user for input

print(str(x) + " * " + str(y) + " = ", end="")
res = input() # result Ergebnis
print("Sie haben geschrieben: " + str(res))

res = input(str(x) + " * " + str(y) + " = ")
