# 유기농 배추

def dfs(x,y):
    visited[x][y]=1

    if y!=0:
        if visited[x][y-1]==0 and graph[x][y-1]==1:
            dfs(x,y-1)

    if y!=m-1:
        if visited[x][y+1]==0 and graph[x][y+1]==1:
            dfs(x,y+1)

    if x!=0:
        if visited[x-1][y]==0 and graph[x-1][y]==1:
            dfs(x-1,y)
        
    if x!=n-1:
        if visited[x+1][y]==0 and graph[x+1][y]==1:
            dfs(x+1,y)

t = int(input())

for _ in range(t):

    m,n,k = map(int,input().split())

    graph=[[0 for _ in range(m)] for _ in range(n)]
    visited=[[0 for _ in range(m)] for _ in range(n)]
    count=0

    for i in range(k):
        x,y=map(int,input().split())
        graph[y][x]=1
        
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and graph[i][j]==1:
                dfs(i,j)
                count+=1

    print(count)