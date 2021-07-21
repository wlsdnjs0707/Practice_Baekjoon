# 다이얼

s = list(input())

dial=0

for i in s:
    if i=='A' or i=='B' or i=='C':
        dial+=3
    elif i=='D' or i=='E' or i=='F':
        dial+=4
    elif i=='G' or i=='H' or i=='I':
        dial+=5
    elif i=='J' or i=='K' or i=='L':
        dial+=6
    elif i=='M' or i=='N' or i=='O':
        dial+=7
    elif i=='P' or i=='Q' or i=='R' or i=='S':
        dial+=8
    elif i=='T' or i=='U' or i=='V':
        dial+=9
    elif i=='W' or i=='X' or i=='Y' or i=='Z':
        dial+=10

print(dial)