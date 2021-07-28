# N과 M (2)

n,m = map(int,input().split())

visited = [0]*n

temp = []

def search(level,n,m):

    if level==m:
        print(' '.join(map(str,temp)))
        return
    
    for i in range(n):
        if visited[i]==0:
            if len(temp)==0:
                visited[i]=1
                temp.append(i+1)
                search(level+1,n,m)
                temp.pop()
                visited[i]=0
            else:
                if temp[level-1]<i+1:
                    visited[i]=1
                    temp.append(i+1)
                    search(level+1,n,m)
                    temp.pop()
                    visited[i]=0
                    
search(0,n,m)