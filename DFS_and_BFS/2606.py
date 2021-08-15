# 바이러스

n = int(input()) # 노드의 수
m = int(input()) # 간선의 수
count=0
graph=[[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(m):
    x,y=map(int,input().split())
    graph[x][y]=graph[y][x]=1

visited=[0 for _ in range(n+1)]

def dfs(v):

    visited[v]=1

    global count
    count+=1

    for i in range(1,n+1):
        if visited[i]==0 and graph[v][i]==1:
            dfs(i)

dfs(1)
print(count-1)