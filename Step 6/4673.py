# 셀프 넘버

def self_numbering(a:list):
    for i in range(1,10000):

        number = i

        while number<10000:
            if number<10:
                number = number + number
            elif number<100:
                number = number + number//10 + (number - (number//10)*10)
            elif number<1000:
                number = number + number//100 + (number - (number//100)*100)//10 + (number - (number//100)*100 - (number//10)*10)
            elif number<10000:
                number = number + number//1000 + (number - (number//1000)*1000)//100 + (number - (number//1000)*1000 - (number//100)*100)//10 + (number - (number//1000)*1000 - (number//100)*100 - (number//10)*10)
            
            if number<10000:
                a[number-1] = 0

a = []

for i in range(10000):
    a.append(i+1)

self_numbering(a)

for i in a:
    if i!=0:
        print(i)