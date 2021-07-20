# 알파벳 찾기

def find_alphabet(s:list):
    list_alphabet = [-1]*26
    for i in range(len(s)):
        if s[i]=='a' and list_alphabet[0]==-1:
            list_alphabet[0] = i
        elif s[i]=='b' and list_alphabet[1]==-1:
            list_alphabet[1] = i
        elif s[i]=='c' and list_alphabet[2]==-1:
            list_alphabet[2] = i
        elif s[i]=='d' and list_alphabet[3]==-1:
            list_alphabet[3] = i
        elif s[i]=='e' and list_alphabet[4]==-1:
            list_alphabet[4] = i
        elif s[i]=='f' and list_alphabet[5]==-1:
            list_alphabet[5] = i
        elif s[i]=='g' and list_alphabet[6]==-1:
            list_alphabet[6] = i
        elif s[i]=='h' and list_alphabet[7]==-1:
            list_alphabet[7] = i
        elif s[i]=='i' and list_alphabet[8]==-1:
            list_alphabet[8] = i
        elif s[i]=='j' and list_alphabet[9]==-1:
            list_alphabet[9] = i
        elif s[i]=='k' and list_alphabet[10]==-1:
            list_alphabet[10] = i
        elif s[i]=='l' and list_alphabet[11]==-1:
            list_alphabet[11] = i
        elif s[i]=='m' and list_alphabet[12]==-1:
            list_alphabet[12] = i
        elif s[i]=='n' and list_alphabet[13]==-1:
            list_alphabet[13] = i
        elif s[i]=='o' and list_alphabet[14]==-1:
            list_alphabet[14] = i
        elif s[i]=='p' and list_alphabet[15]==-1:
            list_alphabet[15] = i
        elif s[i]=='q' and list_alphabet[16]==-1:
            list_alphabet[16] = i
        elif s[i]=='r' and list_alphabet[17]==-1:
            list_alphabet[17] = i
        elif s[i]=='s' and list_alphabet[18]==-1:
            list_alphabet[18] = i
        elif s[i]=='t' and list_alphabet[19]==-1:
            list_alphabet[19] = i
        elif s[i]=='u' and list_alphabet[20]==-1:
            list_alphabet[20] = i
        elif s[i]=='v' and list_alphabet[21]==-1:
            list_alphabet[21] = i
        elif s[i]=='w' and list_alphabet[22]==-1:
            list_alphabet[22] = i
        elif s[i]=='x' and list_alphabet[23]==-1:
            list_alphabet[23] = i
        elif s[i]=='y' and list_alphabet[24]==-1:
            list_alphabet[24] = i
        elif s[i]=='z' and list_alphabet[25]==-1:
            list_alphabet[25] = i
    
    for i in list_alphabet:
        print(i,end=' ')

s = list(input())

find_alphabet(s)