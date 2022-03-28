from numpy import random

maxCnt = 5
cnt = 0
for i in range(maxCnt):
    x = random.randint(10)
    y = random.randint(10)
    print(str(x) + " * " + str(y) + " = ", end="")
    res = input()
    if int(res) == x*y:
        print("right")
        cnt+=1
    else:
        print("wrong")

print(str(cnt)+" Richtige von " + str(maxCnt) + " insgesamt")