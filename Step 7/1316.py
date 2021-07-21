# 그룹 단어 체커

word = []

alphabet = []

checker = 0

count = 0

n = int(input())

for i in range(n):
    word.append(input())

for i in word:
    temp = list(i)
    for j in range(len(temp)):
        if j!=len(temp)-1:
            if temp[j]!=temp[j+1]:
                for k in alphabet:
                    if k==temp[j]:
                        checker=1
                alphabet.append(temp[j])
        elif j==len(temp)-1:
            if temp[j]!=temp[j-1]:
                for k in alphabet:
                    if k==temp[j]:
                        checker=1
                alphabet.append(temp[j])
    if checker==0:
        count+=1
    alphabet=[]
    temp=[]
    checker=0

print(count)