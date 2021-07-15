# 평균

n = int(input())

num_list = list(map(int,input().split()))

print(num_list)

max_num = 0

for i in range(n):
    if num_list[i] > max_num:
        max_num = num_list[i]

for i in range(n):
    num_list[i] = (num_list[i]/max_num)*100

summ = 0

for i in num_list:
    summ = summ + i

print(summ/n)