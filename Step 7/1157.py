# 단어 공부

def find_alphabet(l:list):

    count = [0]*26

    for i in l:
        if i=='a' or i=='A':
            count[0]+=1
        elif i=='b' or i=='B':
            count[1]+=1
        elif i=='c' or i=='C':
            count[2]+=1
        elif i=='d' or i=='D':
            count[3]+=1
        elif i=='e' or i=='E':
            count[4]+=1
        elif i=='f' or i=='F':
            count[5]+=1
        elif i=='g' or i=='G':
            count[6]+=1
        elif i=='h' or i=='H':
            count[7]+=1
        elif i=='i' or i=='I':
            count[8]+=1
        elif i=='j' or i=='J':
            count[9]+=1
        elif i=='k' or i=='K':
            count[10]+=1
        elif i=='l' or i=='L':
            count[11]+=1
        elif i=='m' or i=='M':
            count[12]+=1
        elif i=='n' or i=='N':
            count[13]+=1
        elif i=='o' or i=='O':
            count[14]+=1
        elif i=='p' or i=='P':
            count[15]+=1
        elif i=='q' or i=='Q':
            count[16]+=1
        elif i=='r' or i=='R':
            count[17]+=1
        elif i=='s' or i=='S':
            count[18]+=1
        elif i=='t' or i=='T':
            count[19]+=1
        elif i=='u' or i=='U':
            count[20]+=1
        elif i=='v' or i=='V':
            count[21]+=1
        elif i=='w' or i=='W':
            count[22]+=1
        elif i=='x' or i=='X':
            count[23]+=1
        elif i=='y' or i=='Y':
            count[24]+=1
        elif i=='z' or i=='Z':
            count[25]+=1

    maxnum = 0
    switch = 0

    for j in range(len(count)):

        if count[j]>maxnum:
            maxnum=count[j]
            alphabet=j
        elif maxnum!=0 and count[j]==maxnum:
            switch=1

    if switch==0:
        print(chr(alphabet+65))
    else:
        print('?')

word = list(input())

find_alphabet(word)