# 가장 긴 증가하는 부분 수열

n = int(input())

sequence_list = list(map(int,input().split()))

dp=[0 for _ in range(n)]

# dp = 그 인덱스 값 까지 수열길이의 최댓값

for i in range(n):
    for j in range(i):
        if sequence_list[i]>sequence_list[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1

# 자신보다 작은 숫자들중 가장 큰 길이에+1 한다.

print(dp)