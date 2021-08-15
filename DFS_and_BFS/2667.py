# 단지번호붙이기

n = int(input()) # n by n matrix
matrix=[]

for i in range(n):
    s=list(str(input()))
    matrix.append(list(map(int,s)))

visited=[[0 for _ in range(n)] for _ in range(n)]
temp=[]
answer=[]

def dfs(x,y):
    
    visited[x][y]=1

    temp.append([x,y])

    if y!=0:
        if visited[x][y-1]==0 and matrix[x][y-1]==1:
            dfs(x,y-1)
    
    if y!=n-1:
        if visited[x][y+1]==0 and matrix[x][y+1]==1:
            dfs(x,y+1)

    if x!=0:
        if visited[x-1][y]==0 and matrix[x-1][y]==1:
            dfs(x-1,y)
    
    if x!=n-1:
        if visited[x+1][y]==0 and matrix[x+1][y]==1:
            dfs(x+1,y)

for i in range(n):
    for j in range(n):
        if visited[i][j]==0 and matrix[i][j]==1:
            dfs(i,j)
            if len(temp)!=1:
                answer.append(len(temp))
            temp.clear()

print(len(answer))

for i in answer:
    print(i)