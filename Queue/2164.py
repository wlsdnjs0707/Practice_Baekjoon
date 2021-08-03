# 카드2

n = int(input())

q = [ i for i in range(1,n+1)]

while len(q)>2:
    q.pop(0)
    q.append(q.pop(0))

print(q[1])