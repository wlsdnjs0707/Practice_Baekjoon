# 팩토리얼 0의 개수

n = int(input())

dp=[0 for _ in range(n+1)]

dp[1]=1

for i in range(2,n+1):
    dp[i]=dp[i-1]*i

s = list(map(int,(str(dp[n]))))

count=0

for i in range(len(s)-1,0,-1):
    if s[i]==0:
        count+=1
    else:
        break

print(count)