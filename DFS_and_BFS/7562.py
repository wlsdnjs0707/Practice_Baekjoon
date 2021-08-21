# 나이트의 이동

t = int(input()) # Testcase

for _ in range(t):
    l = int(input()) # l by l board

    current = list(map(int,input().split()))
    destiny = list(map(int,input().split()))

    visited= [[0 for _ in range(l)] for _ in range(l)]

    switch=0

    def bfs(x,y):
        global switch
        queue=[(x,y)]
        visited[y][x]=1
        
        while queue:

            x,y=queue.pop(0)

            if y==destiny[0] and x==destiny[1]:
                switch=1
                return

            if x>=2 and y>=1:
                if visited[x-2][y-1]==0:
                    visited[x-2][y-1]=visited[x][y]+1
                    queue.append((x-2,y-1))

            if x>=2 and y<l-1:
                if visited[x-2][y+1]==0:
                    visited[x-2][y+1]=visited[x][y]+1
                    queue.append((x-2,y+1))

            if x>=1 and y>=2:
                if visited[x-1][y-2]==0:
                    visited[x-1][y-2]=visited[x][y]+1
                    queue.append((x-1,y-2))

            if x>=1 and y<l-2:
                if visited[x-1][y+2]==0:
                    visited[x-1][y+2]=visited[x][y]+1
                    queue.append((x-1,y+2))

            if x<l-1 and y>=2:
                if visited[x+1][y-2]==0:
                    visited[x+1][y-2]=visited[x][y]+1
                    queue.append((x+1,y-2))

            if x<l-1 and y<l-2:
                if visited[x+1][y+2]==0:
                    visited[x+1][y+2]=visited[x][y]+1
                    queue.append((x+1,y+2))

            if x<l-2 and y>=1:
                if visited[x+2][y-1]==0:
                    visited[x+2][y-1]=visited[x][y]+1
                    queue.append((x+2,y-1))

            if x<l-2 and y<l-1:
                if visited[x+2][y+1]==0:
                    visited[x+2][y+1]=visited[x][y]+1
                    queue.append((x+2,y+1))

    bfs(current[1],current[0])

    if switch==1:
        print(visited[destiny[1]][destiny[0]]-1)
    else:
        print(0)