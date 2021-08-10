# 숫자 카드 2

n = int(input())

seq = list(map(int,input().split()))

m = int(input())

seq2 = list(map(int,input().split()))

seq.sort()

def down_binary(target):
    left = 0
    right = len(seq) - 1

    while left <= right:
        mid = (left + right) // 2

        if seq[mid] >= target:
            right = mid - 1
        elif seq[mid] < target:
            left = mid + 1
    return left

def up_binary(target):
    left = 0
    right = len(seq) - 1

    while left <= right:
        mid = (left + right) // 2

        if seq[mid] > target:
            right = mid - 1
        elif seq[mid] <= target:
            left = mid + 1
    return left

for i in range(m):
    print(up_binary(seq2[i])-down_binary(seq2[i]),end=' ')
