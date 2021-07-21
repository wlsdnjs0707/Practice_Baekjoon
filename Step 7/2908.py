# 상수

def changing_number(a,b):
    changed_a = (a%10)*100 + ((a%100)//10)*10 + a//100
    changed_b = (b%10)*100 + ((b%100)//10)*10 + b//100

    if changed_a>changed_b:
        print(changed_a)
    else:
        print(changed_b)

a,b = map(int,input().split())
changing_number(a,b)