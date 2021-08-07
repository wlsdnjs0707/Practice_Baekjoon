# 쿼드트리
import copy
n = int(input())

board=[]

for i in range(n):
    board.append(list(map(int,str(input()))))

result=[0,0,0,0]

def check(x,y,n,level):
    color = board[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if board[i][j]!=color:
                print('(',end='')
                check(x,y,n//2,level+1)
                check(x,y+n//2,n//2,level+1)
                check(x+n//2,y,n//2,level+1)
                check(x+n//2,y+n//2,n//2,level+1)
                print(')',end='')
                return
    
    if color==0:
        print(0,end='')
    else:
        print(1,end='')


check(0,0,n,0)