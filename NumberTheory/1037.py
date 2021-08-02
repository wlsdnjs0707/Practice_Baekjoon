# 약수

n = int(input())

number=list(map(int,input().split()))

summ=1

for i in number:
    summ = summ*i

print(summ)