# 소수 구하기

m,n = map(int,input().split())

check=0
c = []

for i in range(m,n):

    if i==1:
        check=1
    else:
        for j in range(2,i):
            if i%j==0:
                check=1
    
    if check==0:
        c.append(i)

    check=0

for i in c:
    print(i)