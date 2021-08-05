# 덱

from collections import deque

def push_front(d,x):
    d.appendleft(x)

def push_back(d,x):
    d.append(x)

def pop_front(d):
    if len(d)==0:
        print(-1)
    else:
        print(d.popleft())
    
def pop_back(d):
    if len(d)==0:
        print(-1)
    else:
        print(d.pop())

def size(d):
    print(len(d))

def empty(d):
    if len(d)==0:
        print(1)
    else:
        print(0)

def front(d):
    if len(d)==0:
        print(-1)
    else:
        print(d[0])

def back(d):
    if len(d)==0:
        print(-1)
    else:
        print(d[-1])

n = int(input())

d = deque()

for i in range(n):
    c=list(input().split())

    if c[0]=='push_front':
        push_front(d,int(c[1]))
    elif c[0]=='push_back':
        push_back(d,int(c[1]))
    elif c[0]=='pop_front':
        pop_front(d)
    elif c[0]=='pop_back':
        pop_back(d)
    elif c[0]=='size':
        size(d)
    elif c[0]=='empty':
        empty(d)
    elif c[0]=='front':
        front(d)
    elif c[0]=='back':
        back(d)