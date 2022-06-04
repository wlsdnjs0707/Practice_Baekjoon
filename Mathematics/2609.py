# 최대공약수와 최소공배수

gcd = 0
lcm = 0

a,b = map(int,input().split())

if a>=b:
    n = b
else:
    n = a

for i in range(1,n+1):
    if a%i==0 and b%i==0:
        gcd = i

lcm = a*b/gcd

print(gcd)
print(int(lcm))
