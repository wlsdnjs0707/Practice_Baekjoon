# 행렬 곱셈

n,m = map(int,input().split())

A=[]
B=[]
answer=[[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    A.append(list(map(int,input().split())))

m,k = map(int,input().split())

for i in range(m):
    B.append(list(map(int,input().split())))

index=0

while index<m:

    for i in range(n):
        for j in range(n):
            answer[i][j]+=(A[i][index]*B[index][j])
    
    index+=1

for i in range(n):
    for j in range(n):
        if j==n-1:
            print(answer[i][j])
        else:
            print(answer[i][j],end=' ')