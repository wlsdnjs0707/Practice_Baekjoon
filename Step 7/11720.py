# 숫자의 합

n = int(input())

a = list(str(int(input())))
a = list(map(int,a))

summ = 0

for i in a:
    summ = summ + i

print(summ)