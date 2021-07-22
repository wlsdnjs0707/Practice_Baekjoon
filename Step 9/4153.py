# 직각삼각형

while True:
    a,b,c = map(int,input().split())
    if a==0 and b==0 and c==0:
        break

    if a>b:
        temp=b
        b=a
        a=temp

    if b>c:
        temp=c
        c=b
        b=temp

    if a*a+b*b==c*c:
        print("right")
    else:
        print('wrong')