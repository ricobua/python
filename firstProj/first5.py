from numpy import random

maxCnt = 5

for i in range(maxCnt):
  print(i)

input()
print("---------")

cnt = 0
for i in range(maxCnt):
  if (i==7):
    cnt+=1
print("Found 7 that many times: "+str(cnt))

input()
print("---------")

cnt = 0
for i in range(maxCnt):
  x = random.randint(10)
  if (x==2):
    cnt+=1
print("Found 2 that many times: "+str(cnt))