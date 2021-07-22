# 소수

m = int(input())
n = int(input())

check=0
list_check=[]

for i in range(m,n):
    if i==1:
        check=1
    else:
        for j in range(2,i):
            if i%j==0:
                check=1
    
    if check==0:
        list_check.append(i)
    
    check=0

summ=0

for i in list_check:
    summ+=i

if len(list_check)==0:
    print('-1')
else:
    print(summ)
    print(list_check[0])