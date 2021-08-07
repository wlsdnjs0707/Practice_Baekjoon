# 종이의 개수

n = int(input())

seq=[]
count=[0,0,0]

for i in range(n):
    seq.append(list(map(int,input().split())))

def check(x,y,n):

    num = seq[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if num!=seq[i][j]:
                check(x,y,n//3)
                check(x,y+n//3,n//3)
                check(x,y+(n//3)*2,n//3)
                check(x+n//3,y,n//3)
                check(x+n//3,y+n//3,n//3)
                check(x+n//3,y+(n//3)*2,n//3)
                check(x+(n//3)*2,y,n//3)
                check(x+(n//3)*2,y+n//3,n//3)
                check(x+(n//3)*2,y+(n//3)*2,n//3)

                return

    if num==0:
        count[1]+=1
    elif num==1:
        count[2]+=1
    elif num==-1:
        count[0]+=1

check(0,0,n)

print(count)