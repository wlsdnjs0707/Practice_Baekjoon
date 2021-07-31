# 1로 만들기

n = int(input())

dp=[0 for _ in range(n)]

for i in range(1,n):
    dp[i]=dp[i-1]+1

    # 2의배수인데 2로 나누는게 횟수가 적을때
    if i%2==0 and dp[i]>dp[i//2]+1:
        dp[i]=dp[i//2]+1
    
    # 3의배수인데 3으로 나누는게 횟수가 적을때
    if i%3==0 and dp[i]>dp[i//3]+1:
        dp[i]=dp[i//3]+1

print(dp)
