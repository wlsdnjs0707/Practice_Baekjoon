# 피보나치 함수

zero = [1,0,1]
one = [0,1,1]

# fibo(0)일때 0이 1번, 1이 0번...

def fibo(n):
    length = len(zero)
    if n>=length:
        for i in range(length,n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("{0} {1}".format(zero[n],one[n]))

t = int(input())

for i in range(t):
    fibo(int(input()))
