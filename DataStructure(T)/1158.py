# 요세푸스 문제

alive = []
dead =[]

n,k = map(int,input().split())

for i in range(n):
    alive.append(i+1)

while len(alive)>1:
    for i in range(k-1):
        alive.append(alive.pop(0))
    dead.append(alive.pop(0))

dead.append(alive.pop())

print('<',end='')
for i in range(len(dead)):
    if i==len(dead)-1:
        print(dead[i],end='')
    else:
        print("{0}, ".format(dead[i]),end='')
print('>')