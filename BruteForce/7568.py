# 덩치

big=[]
rank=[]
n = int(input())

for i in range(n):
    big.append(list(map(int,input().split())))
    rank.append(0)

for i in range(len(big)):
    count=1
    for j in range(len(big)):
        if big[i][0]<big[j][0] and big[i][1]<big[j][1]:
            count+=1
    rank[i]=count

print(rank)