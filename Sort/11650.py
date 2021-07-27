# 좌표 정렬하기

n = int(input())
coordinate=[]

for i in range(n):
    x,y=map(int,input().split())
    coordinate.append([x,y])

for i in range(n):
    for j in range(i,n):
        if coordinate[i][0]>coordinate[j][0]:
            temp=coordinate[i]
            coordinate[i]=coordinate[j]
            coordinate[j]=temp
        elif coordinate[i][0]==coordinate[j][0]:
            if coordinate[i][1]>coordinate[j][1]:
                temp=coordinate[i]
                coordinate[i]=coordinate[j]
                coordinate[j]=temp

for i in range(len(coordinate)):
    print("{0} {1}".format(coordinate[i][0],coordinate[i][1]))
