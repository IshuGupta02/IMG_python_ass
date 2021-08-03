import array
import math
i = int(input())

sum1=0

values=list(map(int,input().split(' ')))
for j in values:
    sum1=sum1+j
values.sort()
# print(sum)
req= 1+math.floor(sum1/2)

# print("sum1: ", sum1)

# print("req: ", req)

found=0
t=0
for k in range(len(values)-1, -1, -1):
    # print("value of k: ", k)
    if(found>=req):
        break
    found=found+values[k]
    t=t+1
print(t)