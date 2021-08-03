# 조합 0의 개수

n,m = map(int,input().split())

# 0<=m<=n 일때 이항계수
# n!/(m!(n-m)!)

dp=[0 for _ in range(n+1)]

dp[1]=1

for i in range(2,n+1):
    dp[i]=dp[i-1]*i

n=int(dp[n]/(dp[m]*dp[n-m]))
number=list(map(int,str(n)))

count=0

for i in range(len(number)-1,0,-1):
    if number[i]==0:
        count+=1
    else:
        break

print(count)