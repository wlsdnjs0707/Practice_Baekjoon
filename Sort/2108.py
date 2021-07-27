# 통계학

n = int(input())

number=[]

for i in range(n):
    number.append(int(input()))

for i in range(n):
    for j in range(i,n):
        if number[i]>number[j]:
            temp=number[i]
            number[i]=number[j]
            number[j]=temp

# 1. 산술평균
summ=0
for i in number:
    summ+=i
print("{:.0f}".format(summ/n))

# 2. 중앙값
print(number[n//2])

# 3. 최빈값
count=0
count_list=[]
for i in range(n):
    for j in range(i,n):
        if number[i]==number[j]:
            count+=1
    count_list.append(count)
    count=0
max_num=0
answer=[]
for i in range(len(count_list)):
    if max_num<count_list[i]:
        max_num=count_list[i]
for i in range(len(count_list)):
    if count_list[i]==max_num:
        answer.append(number[i])
if len(answer)<2:
    print(answer[0])
else:
    print(answer[1])

# 4. 범위
print(number[n-1]-number[0])