# 좌표 압축

n = int(input())

cdn = list(map(int,input().split()))

copy = list(set(cdn))

answer=[]

count = 0

for i in range(len(cdn)):
    for j in range(len(copy)):
        if cdn[i]>copy[j]:
            count+=1
    answer.append(count)
    count=0

print(answer)