# A+B-3
list_a=[]
t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    list_a.append(a+b)

for i in list_a:
    print(i)
