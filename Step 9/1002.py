# 터렛
import math

t = int(input()) # Test case

for i in range(t):

    x1,y1,r1,x2,y2,r2 = map(int,input().split())
    answer = 0
    d = math.sqrt(math.pow(x1-x2,2))+math.sqrt(math.pow(y1-y2,2))


    # Case 4
    if x1==x2 and y1==y2:
        if r1==r2:
            answer=-1
        else:
            answer==0
    # Case 1
    elif d>r1+r2:
        answer=0
    # Case 2
    elif d==r1+r2:
        answer=1
    # Case 3
    elif d<r1+r2:
        if d==abs(r1-r2):
            answer=1
        else:
            answer=2


    print(answer)