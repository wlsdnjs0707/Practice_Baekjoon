# 큐2

def push(q,x):
    q.append(x)

def pop(q):
    if len(q)==0:
        print(-1)
    else:
        print(q.pop(0))

def size(q):
    print(len(q))

def empty(q):
    if len(q)==0:
        print(1)
    else:
        print(0)

def front(q):
    if len(q)==0:
        print(-1)
    else:
        print(q[0])

def back(q):
    if len(q)==0:
        print(-1)
    else:
        print(q[-1])

n = int(input())
q=[]

for i in range(n):
    c=list(input().split())
    if c[0]=='push':
        push(q,int(c[1]))
    elif c[0]=='pop':
        pop(q)
    elif c[0]=='size':
        size(q)
    elif c[0]=='empty':
        empty(q)
    elif c[0]=='front':
        front(q)
    elif c[0]=='back':
        back(q)
    