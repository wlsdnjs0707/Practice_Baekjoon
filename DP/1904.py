# 01타일

n = int(input())
dp = [0]*(n+1)

dp[0]=0
dp[1]=1 #1
dp[2]=2 #11 #00

for i in range(3,n+1):
    dp[i]=(dp[i-1]+dp[i-2])%15746

print(dp[n])