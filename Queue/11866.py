# 요세푸스 문제 0

n,k = map(int,input().split())

q = [ i for i in range(1,n+1)]

j=[]

while len(q)!=0:
    for i in range(k-1):
        q.append(q.pop(0))
    j.append(q.pop(0))

print(j)