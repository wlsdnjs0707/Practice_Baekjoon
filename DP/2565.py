# 전깃줄

n = int(input())

line=[]

for i in range(n):
    x,y=map(int,input().split())
    line.append([x,y])

# 겹침 판정
# x1<x2 and y1>y2

dp=[0 for _ in range(n)]

for i in range(n):
    for j in range(n):
        if line[i][0]<line[j][0]:
            if line[i][1]>line[j][1]:
                dp[i]+=1

print(n-dp.count(0))