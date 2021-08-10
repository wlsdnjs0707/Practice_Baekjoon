# 랜선 자르기

k,n = map(int,input().split())

length=[]

for i in range(k):
    length.append(int(input()))

summ=0

for i in length:
    summ+=i

while True:
    temp=0
    
    for i in range(len(length)):
        temp+=length[i]//summ
    
    if temp>=n:
        break
    else:
        summ-=1
    
print(summ)