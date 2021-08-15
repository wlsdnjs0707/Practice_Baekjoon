# DFS와 BFS
from collections import deque

n,m,v = map(int,input().split())

temp=[]
graph=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    temp.append([x,y])

for i in range(len(temp)):
    x=temp[i][0]
    y=temp[i][1]
    graph[x][y]=graph[y][x]=1


visited=[0 for i in range(m+1)]

def dfs(graph,v,visited):

    visited[v]=1

    print(v)

    for i in range(1,n+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(graph,i,visited)

def bfs(graph,v,visited):
    q = deque([v])

    visited[v]=0

    while q:
        v=q.popleft()
        print(v)
        for i in range(1,n+1):
            if visited[i]==1 and graph[v][i]==1:
                q.append(i)
                visited[i]=0
    

dfs(graph,v,visited)
bfs(graph,v,visited)