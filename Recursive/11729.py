# 하노이 탑 이동 순서

def hanoi(n,a,b,c):
    if n==1:
        print("{0} {1}".format(a,c))
    else:
        hanoi(n-1,a,c,b)
        print("{0} {1}".format(a,c))
        hanoi(n-1,b,a,c)

n = int(input())

print(2**(n)-1)
hanoi(n,1,2,3)