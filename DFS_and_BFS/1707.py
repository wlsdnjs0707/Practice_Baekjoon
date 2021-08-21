# 이분 그래프

k = int(input()) #Testcase

for _ in range(k):
    
    graph=[]
    switch=0

    v,e = map(int,input().split())

    for _ in range(e):
        x,y=map(int,input().split())
        if x>y:
            graph.append([y,x])
        else:
            graph.append([x,y])

    visited = [0 for _ in range(v+1)]

    queue=[graph[0][0]]
    visited[graph[0][0]]=1

    while queue:
        index = queue.pop(0)

        for i in range(e):
            if graph[i][0]==index:
                if visited[graph[i][1]]==0:
                    visited[graph[i][1]]=1
                    queue.append(graph[i][1])
                elif visited[graph[i][1]]==1:
                    switch=1
                    break

    if switch==0:
        print('YES')
    else:
        print('NO')