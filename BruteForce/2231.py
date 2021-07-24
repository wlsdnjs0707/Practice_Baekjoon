# 분해합

n = int(input())

num = 0
answer=[]

for i in range(1,n):
    num=0
    for j in range(1,7):
        if i>=10**(j-1) and i<10**j:
            for k in range(j,-1,-1):
                num+=(i//(10**k))%10

    num+=i

    if num==n:
        answer.append(i)

if len(answer)==0:
    print(0)
else:
    print(answer[0])