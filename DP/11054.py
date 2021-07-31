# 가장 긴 바이토닉 부분 수열

from sys import hexversion


n = int(input())

seq=list(map(int,input().split()))

dp = [1 for _ in range(n)]
dp2 = [1 for _ in range(n)]
# 바이토닉 수열 = 증가하는 수열 + 감소하는 수열

for i in range(n):
    for j in range(i):
        if seq[i]>seq[j]:
            dp[i]=max(dp[i],dp[j]+1)

for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if seq[i]>seq[j]:
            dp2[i]=max(dp2[i],dp2[j]+1)

result=[0 for _ in range(n)]

for i in range(n):
    result[i]=dp[i]+dp2[i]-1

print(max(result))