# 블랙잭

n,m = map(int,input().split())

number = list(map(int,input().split()))

summ=0
new_summ=0

for i in range(len(number)):
    for j in range(len(number)):
        if i!=j:
            for k in range(len(number)):
                if i!=k and j!=k:
                    new_summ = number[i]+number[j]+number[k]
                if new_summ<=m and summ<new_summ:
                    summ=new_summ

print(summ)