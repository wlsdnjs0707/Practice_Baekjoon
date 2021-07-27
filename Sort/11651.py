# 좌표 정렬하기 2

n = int(input())

cdn = []

for i in range(n):
    x,y=map(int,input().split())
    cdn.append([x,y])

for i in range(n):
    for j in range(i,n):
        if cdn[i][1]>cdn[j][1]:
            temp=cdn[i]
            cdn[i]=cdn[j]
            cdn[j]=temp
        elif cdn[i][1]==cdn[j][1]:
            if cdn[i][0]>cdn[j][0]:
                temp=cdn[i]
                cdn[i]=cdn[j]
                cdn[j]=temp

for i in range(n):
    print("{0} {1}".format(cdn[i][0],cdn[i][1]))

