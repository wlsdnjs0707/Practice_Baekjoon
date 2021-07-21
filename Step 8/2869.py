# 달팽이는 올라가고 싶다

a,b,v = map(int,input().split())

# 낮 = a / 밤 = b / 막대길이 = v

height = 0
day = 0

day = ((v//(a-b))-a) * (a-b)
height = day*(a-b)

while True:
    day+=1
    height+=a
    if height>=v:
        break
    else:
        height-=b

print(day)