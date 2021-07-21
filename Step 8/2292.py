# 벌집

count = 0

n = int(input())

i = 1

if n==1:
    print(1)
elif n<8:
    print(2)
else:
    while count<=n:
        count = count + i*6
        i+=1
    print(i)