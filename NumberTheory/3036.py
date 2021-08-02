# 링

n = int(input())

r = list(map(int,input().split()))

s = r[0]

def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

for i in range(1,n):
    if s>=i:
        print("{0}/{1}".format(int(s/gcd(s,r[i])),int(r[i]/gcd(s,r[i]))))
    else:
        print("{0}/{1}".format(int(s/gcd(r[i],s)),int(r[i]/gcd(r[i],s))))
