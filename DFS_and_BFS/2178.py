# 미로 탐색
# BFS

n,m = map(int,input().split())
# m * n matrix
graph=[]

for i in range(n):
    s = str(input())
    graph.append(list(map(int,s)))

visited=[[0 for _ in range(m)] for _ in range(n)]

def bfs(x,y):
    queue=[(x,y)]
    visited[x][y]=1

    while queue:
        x,y=queue.pop(0)

        if x==n-1 and y==m-1:
            print(visited[x][y])
            break
        
        if y!=0:
            if visited[x][y-1]==0 and graph[x][y-1]==1:
                visited[x][y-1]=visited[x][y]+1
                queue.append((x,y-1))
        if y!=m-1:
            if visited[x][y+1]==0 and graph[x][y+1]==1:
                visited[x][y+1]=visited[x][y]+1
                queue.append((x,y+1))

        if x!=0:
            if visited[x-1][y]==0 and graph[x-1][y]==1:
                visited[x-1][y]=visited[x][y]+1
                queue.append((x-1,y))

        if x!=n-1:
            if visited[x+1][y]==0 and graph[x+1][y]==1:
                visited[x+1][y]=visited[x][y]+1
                queue.append((x+1,y))

bfs(0,0)