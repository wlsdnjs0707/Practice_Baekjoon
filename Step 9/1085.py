# 직사각형에서 탈출

x,y,w,h = map(int,input().split())

d = []

d.append(x)
d.append(y)
d.append(w-x)
d.append(h-y)

small=x+y+w+h

for i in d:
    if small>i:
        small=i

print(small)