# 주유소

n = int(input())

d=list(map(int,input().split())) # distance # 0 : 1번째-2번째 사이의 거리
p=list(map(int,input().split())) # oil price # 0 : 1번째 나라의 기름 가격

index_before=0
index_after=0
summ=0
total=0

for i in range(n):
    if p[0]>p[i]:
        index_before=i
        break
    elif i==n-1:
        index=i
for i in range(index_before):
    summ+=d[i]
total+=summ*p[0]
summ=0

while True:
    if index_before==n-1:
        break
    for i in range(index_before,n):
        if p[index_before]>p[i]:
            index_after=i
            break
        elif i==n-1:
            index_after=i
    for i in range(index_before,index_after):
        summ+=d[i]
    total+=summ*p[index_before]
    summ=0
    index_before=index_after

print(total)