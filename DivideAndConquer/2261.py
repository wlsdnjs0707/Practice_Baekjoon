import math
# 가장 가까운 두 점

n = int(input())

co=[]
answer=[]

for i in range(n):
    x,y=map(int,input().split())
    co.append([x,y])

for i in range(n):
    for j in range(i+1,n):
        answer.append(math.pow(abs(co[i][0]-co[j][0]),2)+math.pow(abs(co[i][1]-co[j][1]),2))

print(int(min(answer)))