# 정수 N개의 합

def solve(a:list):
    summ = 0
    for i in a:
        summ = summ + i
    print(summ)

num_list = list(map(int,input().split()))

solve(num_list)