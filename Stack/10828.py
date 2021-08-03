# 스택

def push(q,x):
    q.append(x)

def pop(q):
    if len(q)==0:
        print(-1)
    else:
        print(q.pop())

def size(q):
    print(len(q))

def empty(q):
    if len(q)==0:
        print(1)
    else:
        print(0)

def top(q):
    if len(q)==0:
        print(-1)
    else:
        print(q[-1])

n = int(input())

q=[]

for i in range(n):
    command=list(input().split())
    if command[0]=='push':
        push(q,command[1])
    elif command[0]=='pop':
        pop(q)
    elif command[0]=='size':
        size(q)
    elif command[0]=='empty':
        empty(q)
    elif command[0]=='top':
        top(q)