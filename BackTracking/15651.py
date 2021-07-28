# N과 M (3)

n,m=map(int,input().split())

temp = []

def search(level,n,m):

    if level==m:
        print(' '.join(map(str,temp)))
        return

    for i in range(n):
        temp.append(i+1)
        search(level+1,n,m)
        temp.pop()

search(0,n,m)