# ATM

n = int(input())

s = list(map(int,input().split()))

s.sort()

summ=0

for i in range(n+1):
    for j in range(i):
        summ+=s[j]

print(summ)