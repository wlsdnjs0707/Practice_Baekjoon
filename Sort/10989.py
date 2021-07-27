# 수 정렬하기 3
# Counting Sort

n = int(input())

a = []

for i in range(n):
    a.append(int(input()))

max_num = max(a)

index = [0]*max_num

for i in a:
    index[i-1]+=1

print(index)

for i in range(len(index)):
    for j in range(index[i]):
        print(i+1)