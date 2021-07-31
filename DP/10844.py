# 쉬운 계단 수

n = int(input())

dp=[0 for _ in range(n+1)]

dp[0]=0
dp[1]=9

# dp[n]=dp[n-1]*2-(n-1)

for i in range(2,n+1):
    dp[i]=((dp[i-1]*2)-(i-1))%1000000000

print(dp[n])