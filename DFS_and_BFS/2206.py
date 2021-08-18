# 벽 부수고 이동하기
import copy

n,m = map(int,input().split())
graph=[]

for i in range(n):
    temp = list(map(int,str(input())))
    graph.append(temp)

g_copy = copy.deepcopy(graph)

visited=[[0 for _ in range(m)] for _ in range(n)]

v_copy = copy.deepcopy(visited)

def bfs(x,y):
    switch=0
    answer=0

    queue=[(x,y)]
    visited[x][y]=1

    while queue:
        x,y=queue.pop(0)

        if x==n-1 and y==m-1:
            switch=1
            break

        if y!=0:
            if visited[x][y-1]==0 and graph[x][y-1]==0:
                visited[x][y-1]=visited[x][y]+1
                graph[x][y-1]=1
                queue.append((x,y-1))
        if y!=m-1:
            if visited[x][y+1]==0 and graph[x][y+1]==0:
                visited[x][y+1]=visited[x][y]+1
                graph[x][y+1]=1
                queue.append((x,y+1))
        if x!=0:
            if visited[x-1][y]==0 and graph[x-1][y]==0:
                visited[x-1][y]=visited[x][y]+1
                graph[x-1][y]=1
                queue.append((x-1,y))
        if x!=n-1:
            if visited[x+1][y]==0 and graph[x+1][y]==0:
                visited[x+1][y]=visited[x][y]+1
                graph[x+1][y]=1
                queue.append((x+1,y))

    for i in range(n):
        for j in range(m):
            if answer<visited[i][j]:
                answer=visited[i][j]

    if switch==1:
        answer_list.append(answer-1)
    else:
        answer_list.append(-1)

answer_list=[]

bfs(0,0)
graph=copy.deepcopy(g_copy)
visited=copy.deepcopy(v_copy)
dist=n*m+1

for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            graph[i][j]=0
            bfs(0,0)
            graph=copy.deepcopy(g_copy)
            visited=copy.deepcopy(v_copy)

for i in answer_list:
    if i!=-1:
        if i<dist:
            dist=i

if dist==n*m+1:
    print(-1)
else:
    print(dist+1)