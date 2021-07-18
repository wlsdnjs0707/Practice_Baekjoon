# 셀프 넘버

def self_numbering(a:list):
    for i in range(1,10000):

        number = i

        if number<10:
            nn = number + number
            # 1 = 1 + 1
        elif number<100:
            nn = number + number//10 + number%10
            # 12 = 12 + 1 + 2
        elif number<1000:
            nn = number + number//100 + (number%100)//10 + number%10
            # 123 = 123 + 1 + 2 + 3
        elif number<10000:
            nn = number + number//1000 + (number%1000)//100 + (number%100)//10 + number%10
            # 1234 = 1234 + 1 + 2 + 3 + 4
        
        if nn<=10000:
            a[nn-1] = 0

a = []

for i in range(10000):
    a.append(i+1)

self_numbering(a)

for i in a:
    if i!=0:
        print(i)