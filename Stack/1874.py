# 스택 수열

n = int(input())
number=[]
temp=[]
index_1=0
index_2=1
answer=[]
operator=[]

for i in range(n):
    number.append(int(input()))

while len(answer)<=n and len(temp)<=n:

    if len(answer)==len(number):
        break

    if len(temp)==0:
        temp.append(index_2)
        operator.append('+')
        index_2+=1

    if temp[-1]==number[index_1]:
        answer.append(temp.pop())
        operator.append('-')
        index_1+=1
    else:
        temp.append(index_2)
        operator.append('+')
        index_2+=1
    
if len(answer)==len(number):
    for i in operator:
        print(i)
else:
    print('NO')