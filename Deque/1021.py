# 회전하는 큐

from collections import deque

d = deque()

n,m = map(int,input().split())

for i in range(n):
    d.append(i)

numbers=list(map(int,input().split()))

for i in range(len(numbers)):
    numbers[i]-=1

count=0

for i in range(m):
    index=0

    for j in range(len(d)):
        if numbers[i]==d[j]:
            index=j

    while index!=0:
        if index < (len(d)/2):
            d.rotate(-1)
            count+=1
            index-=1
        elif index >= (len(d)/2):
            d.rotate(1)
            count+=1
            if index==len(d)-1:
                index=0
            else:
                index+=1
    
    d.popleft()

print(count)