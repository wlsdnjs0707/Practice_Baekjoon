# 검문

n = int(input())

number=[]
switch=0
answer=[]

for i in range(n):
    number.append(int(input()))

for i in range(2,max(number)):
    for j in range(1,n-1):
        if number[j]%i!=number[j+1]%i:
            switch=1
    if switch==0:
        answer.append(i)
    switch=0

print(answer)