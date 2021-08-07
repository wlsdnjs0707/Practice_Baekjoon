# 색종이 만들기

import sys

n = int(input())

board=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]

result=[]

def check(x,y,n):
    
    color = board[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if color != board[i][j]:
                check(x,y,int(n//2))
                check(x,y+int(n//2),int(n//2))
                check(x+int(n//2),y,int(n//2))
                check(x+int(n//2),y+int(n//2),n//2)
                return
    
    if color==0:
        result.append(0)
    else:
        result.append(1)

check(0,0,n)
print(result.count(0))
print(result.count(1))
