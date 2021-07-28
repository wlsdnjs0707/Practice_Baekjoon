# N과 M (1)

n,m = map(int,input().split())

visited = [0]*n

temp = []

def search(level,n,m):

    if level==m: #수열의 길이가 m일때
        print(' '.join(map(str,temp)))
        return
    
    for i in range(len(visited)):
        if visited[i]==0:
            visited[i]=1
            temp.append(i+1)
            search(level+1,n,m)
            temp.pop()
            visited[i]=0

search(0,n,m)