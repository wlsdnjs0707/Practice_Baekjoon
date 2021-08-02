# 동전 0

n,k = map(int,input().split())
coin=[]
count=0

for i in range(n):
    coin.append(int(input()))

r = k

for i in range(n-1,0,-1):
    if coin[i]<r:
        count+=r//coin[i]
        r=r%coin[i]

print(count)