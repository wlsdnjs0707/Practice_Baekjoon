# 더하기 사이클

newnum = 0
cycle =0

n = int(input())

newnum = n

while True:

    if n<10:
        n = 10*n
    
    n = (n%10)*10 + (n//10+n%10) % 10
    
    cycle = cycle + 1

    if n == newnum:
        break

print(cycle)