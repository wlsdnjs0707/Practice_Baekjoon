# RGB거리

n = int(input())

rgb=[]

cost=0
index=0
answer=[]

for i in range(n):
    rgb.append(list(map(int,input().split())))

for i in range(3):
    cost=rgb[0][i]
    index=i
    for j in range(1,n):
        if index==0:
            if rgb[j][1]<rgb[j][2]:
                cost+=rgb[j][1]
                index=1
            elif rgb[j][1]>rgb[j][2]:
                cost+=rgb[j][2]
                index=2
            else:
                cost+=rgb[j][1]
                index=1
        elif index==1:
            if rgb[j][0]<rgb[j][2]:
                cost+=rgb[j][0]
                index=0
            elif rgb[j][0]>rgb[j][2]:
                cost+=rgb[j][2]
                index=2
            else:
                cost+=rgb[j][0]
                index=0
        elif index==2:
            if rgb[j][0]<rgb[j][1]:
                cost+=rgb[j][0]
                index=0
            elif rgb[j][0]>rgb[j][1]:
                cost+=rgb[j][1]
                index=1
            else:
                cost+=rgb[j][0]
                index=0
    answer.append(cost)

print(min(answer))