# 숨바꼭질

n,k = map(int,input().split())
visited=[0 for _ in range(100001)]
def bfs(v):
    count=0

    queue=[[v,count]]

    while queue:
        e,count=queue.pop(0)
        visited[e]=1
        
        if e==k:
            return count
        
        count+=1
        
        if e*2 <= 100000:
            queue.append([e*2,count])
        if e+1 <= 100000:
            queue.append([e+1,count])
        if e-1 >= 0:
            queue.append([e-1,count])

    return count

print(bfs(n))