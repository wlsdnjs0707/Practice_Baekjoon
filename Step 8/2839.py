# 설탕 배달

n = int(input())
switch=0
count = 0
res = n

if n%5==0:
    count=n//5
else:
    count = n//5
    res = n%5

    while res!=0:
        if res%3==0:
            count+=res//3
            res=0
        else:
            res=res+5
            count-=1

        if count<0:
            break

if count<0:
        print(-1)
else:
        print(count)