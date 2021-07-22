# 소인수분해

n = int(input())

d = []

res = n

i=2

while res>1:
    if res%i==0:
        d.append(i)
        res=int(res/i)
    else:
        i+=1

for i in d:
    print(i)