# A+B-8

clist = []

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    clist.append([a,b,a+b])

for i in range(len(clist)):
    print("Case #{0}: {1} + {2} = {3}".format(i+1,clist[i][0],clist[i][1],clist[i][2]))

