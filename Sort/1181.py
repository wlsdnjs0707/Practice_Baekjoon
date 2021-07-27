# 단어 정렬

n = int(input())

s = []

for i in range(n):
    s.append(input())

s=set(s)
s=list(s)

for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            print('hit')

for i in range(len(s)):
    for j in range(i+1,len(s)):
        temp1=list(s[i])
        temp2=list(s[j])

        print(temp1,temp2)

        if len(temp1)>len(temp2):
            temp=s[i]
            s[i]=s[j]
            s[j]=temp
        elif len(temp1)==len(temp2):
            count=0
            while count<len(temp1):
                if temp1[count]==temp2[count]:
                    count+=1
                else:
                    if ord(temp1[count])>ord(temp2[count]):
                        temp=s[i]
                        s[i]=s[j]
                        s[j]=temp
                    break

for i in s:
    print(i)