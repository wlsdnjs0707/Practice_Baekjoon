# 나머지

num_list = []

for i in range(10):
    num_list.append(int(input()))

for i in range(10):
    num_list[i] = num_list[i] % 42

set_list = set(num_list)

print(len(set_list))