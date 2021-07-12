# 빠른 A+B
# input() 대신 sys.stdin.readline()을 사용
# 시간이 빠르다

import sys

t = int(sys.stdin.readline())

for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print(a+b)
