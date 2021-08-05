# AC

from collections import deque

T = int(input()) # Test case

for _ in range(T):
    p = list(input())
    n = int(input())
    seq=list(input().split(','))
    temp=deque()
    switch=0
    temp1=[]

    if n==0:
        temp=deque()
    elif len(seq)==1:
        temp1=list(str(seq[0]))
        temp1=deque(temp1)
        temp1.pop()
        temp1.popleft()
        temp1=''.join(temp1)
        temp.append(int(temp1))
    else:
        for i in range(len(seq)):
            if i==0:
                temp1=list(str(seq[i]))
                temp1=deque(temp1)
                temp1.popleft()
                temp1=''.join(temp1)
                temp.append(int(temp1))
            elif i==len(seq)-1:
                temp1=list(str(seq[i]))
                temp1=deque(temp1)
                temp1.pop()
                temp1=''.join(temp1)
                temp.append(int(temp1))
            else:
                temp.append(int(seq[i]))

    for i in range(len(p)):
        if p[i]=='R':
            temp.reverse()
        elif p[i]=='D':
            if len(temp)==0:
                switch=1
            else:
                temp.popleft()
    
    if switch==0:       
        print('[',end='')
        for i in range(len(temp)):
            if i==len(temp)-1:
                print(temp[i],end='')
            else:
                print('{0},'.format(temp[i]),end='')
        print(']')
    else:
        print('error')