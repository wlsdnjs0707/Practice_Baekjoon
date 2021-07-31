# 계단 오르기

n = int(input())

stair=[]

for i in range(n):
    stair.append(int(input()))

# n번째 계단에서 나올수 있는 최대값
# max(n+(n-1)+(n-3),n+(n-2)+(n-3))

dp=[0 for _ in range(n)]

dp[0]=stair[0]
dp[1]=stair[0]+stair[1]
dp[2]=max(stair[0],stair[1])+stair[2]

for i in range(3,n):
    dp[i]=stair[i]+max(dp[i-3]+stair[i-1],dp[i-2])
# max(전계단 밟은경우,전계단 안밟은경우)

print(dp[n-1])