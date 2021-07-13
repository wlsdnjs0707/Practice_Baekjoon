# A+B-5

nlist = []
a = 1
b = 1

while True:
    a,b = map(int,input().split())
    if a==0 and b==0 :
        break
    nlist.append(a+b)

for i in nlist:
    print(i)