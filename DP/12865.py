# 평범한 배낭

n,k = map(int,input().split())

stuff=[[0,0]]

for i in range(n):
    w,v=map(int,input().split())
    stuff.append([w,v])

dp=[[0 for _ in range(k+1)] for _ in range(n+1)]

# dp[i][j] = max(현재가치+dp[이전물건][남은무게-현재물건무게],dp[이전물건][남은무게])

for i in range(n+1):
    for j in range(k+1):
        weight = stuff[i][0]
        value = stuff[i][1]

        if j<weight:
            dp[i][j]=dp[i-1][j]
            # 남은 무게가 weight보다 작으면 위값을 그대로 가져온다(패스)
        else:
            dp[i][j]=max(value+dp[i-1][j-weight],dp[i-1][j])
            # (현재물건돌기전 최댓값 vs 현재무게 뺀 것까지의 최댓값+현재가치)중에 더 큰값 넣어준다.

print(dp)
print(dp[n][k])