# X보다 작은 수

n,x = map(int,input().split())

nlist = list(map(int,input().split()))
alist = []

for i in range(n):
    if nlist[i] < x :
        alist.append(nlist[i])

for i in alist:
    print(i,end=' ')