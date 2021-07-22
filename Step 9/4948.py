# 베르트랑 공준

while True:

    n = int(input())
    
    if n==0:
        break

    d=[]
    check=0

    for i in range(n+1,(2*n)+1):
        if i==1:
            check=1
        else:
            for j in range(2,i):
                if i%j==0:
                    check=1
        if check==0:
            d.append(i)
        check=0
    
    print(len(d))