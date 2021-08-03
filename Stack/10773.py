# 제로

k = int(input())

s=[]

for i in range(k):
    num=int(input())

    if num==0:
        s.pop()
    else:
        s.append(num)

print(sum(s))