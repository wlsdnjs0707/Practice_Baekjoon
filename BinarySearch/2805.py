# 나무 자르기

n,m = map(int,input().split())

h = list(map(int,input().split()))

index = max(h)

while True:
    summ=0

    for i in range(len(h)):
        if index>=h[i]:
            summ+=0
        else:
            summ+=(h[i]-index)
    
    if summ>=m:
        break
    else:
        index-=1

print(index)