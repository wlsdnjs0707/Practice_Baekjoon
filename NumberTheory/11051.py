# 이항 계수 2
# 동적 계획법 사용

n,k = map(int,input().split())

dp=[0 for _ in range(n+1)]
dp[0]=0
dp[1]=1

for i in range(2,n+1):
    dp[i]=(dp[i-1]*i)%10007

print(int(dp[n]/(dp[k]*dp[n-k])))