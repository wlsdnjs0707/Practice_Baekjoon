# 토마토

m,n = map(int,input().split())
graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

visited=[[0 for _ in range(m)] for _ in range(n)]

def bfs(queue):
    while queue:
        x,y = queue.pop(0)
        if y!=0:
            if visited[x][y-1]==0 and graph[x][y-1]==0:
                graph[x][y-1]=1
                visited[x][y-1]=visited[x][y]+1
                queue.append((x,y-1))
        if y!=m-1:
            if visited[x][y+1]==0 and graph[x][y+1]==0:
                graph[x][y+1]=1
                visited[x][y+1]=visited[x][y]+1
                queue.append((x,y+1))
        if x!=0:
            if visited[x-1][y]==0 and graph[x-1][y]==0:
                graph[x-1][y]=1
                visited[x-1][y]=visited[x][y]+1
                queue.append((x-1,y))
        if x!=n-1:
            if visited[x+1][y]==0 and graph[x+1][y]==0:
                graph[x+1][y]=1
                visited[x+1][y]=visited[x][y]+1
                queue.append((x+1,y))

queue=[]

for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==0:
            queue.append((i,j))
            visited[i][j]=1
bfs(queue)
answer=0

for i in range(n):
    for j in range(m):
        if visited[i][j]>answer:
            answer=visited[i][j]

switch=0
for i in range(n):
    if 0 not in graph[i]:
        continue
    else:
        switch=1

if switch==0:
    print(answer-1)
else:
    print(-1)