# 포도주 시식

n = int(input())

score=[0]

for i in range(n):
    score.append(int(input()))

# dp[n] = score[n] + max(dp[n-3]+score[n-1],dp[n-2],dp[n-1])
# 해당 단계 안마시는경우 / 마시는경우 - 그전단계 마시는경우, 안마시는경우
# 총 3가지중 max를 찾는다

dp=[0 for _ in range(n+1)]
dp[0]=0
dp[1]=score[1]

if n>1:
    dp[2]=score[1]+score[2]

for i in range(3,n+1):
    dp[i]=max(dp[i-1],dp[i-3]+score[i-1]+score[i],dp[i-2]+score[i])

print(dp[n])