# 최소 공배수

def gcd(x,y):
    while y>0:
        x,y=y,x%y
    return x

t = int(input())

for i in range(t):
    a,b = map(int,input().split())

    temp=0

    if a>b:
        temp=gcd(a,b)
    else:
        temp=gcd(b,a)

    print(int(a*b//temp))