# 최대공약수와 최소공배수

a,b = map(int,input().split())

gcd=0 #Greatest common divisor
lcm=0 #Largest common multiple

for i in range(1,min(a,b)):
    if a%i==0 and b%i==0:
        gcd=i

lcm = a*b/gcd

print(gcd)
print(int(lcm))