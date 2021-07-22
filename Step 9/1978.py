# 소수 찾기

n = int(input())

list_number = list(map(int,input().split()))

list_check = []

checker = 0

for i in list_number:
    if i==1:
        checker=1
    else:
        for j in range(2,i):
            if i%j==0:
                checker=1
    if checker==0:
        list_check.append(1)
    checker=0

print(len(list_check))