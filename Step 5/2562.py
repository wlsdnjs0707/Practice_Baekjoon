# 최댓값

num_list = []

for i in range(9):
    num_list.append(int(input()))

print(max(num_list))

for i in range(9):
    if num_list[i] == max(num_list):
        print(i+1)