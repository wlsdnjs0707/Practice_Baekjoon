# 연속합

n = int(input())

seq = list(map(int,input().split()))

dp=[]

for i in range(n):
    dp.append(seq[i])

summ=0

for i in range(n+1):
    for j in range(i):
        for k in range(j,i):
            summ+=seq[k]
        if dp[i-1]<summ:
            dp[i-1]=summ
        summ=0

print(max(dp))