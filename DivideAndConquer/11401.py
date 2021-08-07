# 이항 계수 3

n,k = map(int,input().split())

# 이항계수 (n,k) = n!/(n-k!)k!

dp=[0 for _ in range(n+1)]

dp[1]=1

for i in range(2,n+1):
    dp[i]=dp[i-1]*i

print(int((dp[n]/(dp[n-k]*dp[k]))%1000000007))