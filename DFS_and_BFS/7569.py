# 토마토

m,n,h = map(int,input().split())
graph=[]
temp=[]
temp1=[]
visited=[[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
for i in range(h):
    for j in range(n):
        temp.append(list(map(int,input().split())))
    temp1=temp.copy()
    graph.append(temp1)
    temp.clear()

def bfs(queue):
    
    while queue:
        x,y,z = queue.pop(0)

        if z!=0:
            if visited[x][y][z-1]==0 and graph[x][y][z-1]==0:
                graph[x][y][z-1]=1
                visited[x][y][z-1]=visited[x][y][z]+1
                queue.append((x,y,z-1))
        if z!=m-1:
            if visited[x][y][z+1]==0 and graph[x][y][z+1]==0:
                graph[x][y][z+1]=1
                visited[x][y][z+1]=visited[x][y][z]+1
                queue.append((x,y,z+1))        
        if y!=0:
            if visited[x][y-1][z]==0 and graph[x][y-1][z]==0:
                graph[x][y-1][z]=1
                visited[x][y-1][z]=visited[x][y][z]+1
                queue.append((x,y-1,z))
        if y!=n-1:
            if visited[x][y+1][z]==0 and graph[x][y+1][z]==0:
                graph[x][y+1][z]=1
                visited[x][y+1][z]=visited[x][y][z]+1
                queue.append((x,y+1,z))
        if x!=0:
            if visited[x-1][y][z]==0 and graph[x-1][y][z]==0:
                graph[x-1][y][z]=1
                visited[x-1][y][z]=visited[x][y][z]+1
                queue.append((x-1,y,z))
        if x!=h-1:
            if visited[x+1][y][z]==0 and graph[x+1][y][z]==0:
                graph[x+1][y][z]=1
                visited[x+1][y][z]=visited[x][y][z]+1
                queue.append((x+1,y,z))

queue=[]
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1 and visited[i][j][k]==0:
                queue.append((i,j,k))
                visited[i][j][k]=1

bfs(queue)
switch=0
answer=0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==0:
                switch=1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if answer<visited[i][j][k]:
                answer=visited[i][j][k]

if switch==1:
    print(-1)
else:
    print(answer-1)