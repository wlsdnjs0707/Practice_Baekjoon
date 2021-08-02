# 잃어버린 괄호

s = list(input())

for i in range(len(s)):
    if s[i]!='+' and s[i]!='-':
        s[i]=int(s[i])

temp=[]
s2=[]
summ=0

for j in range(len(s)):
    if type(s[j])==int:
        temp.append(s[j])
    else:
        for i in range(len(temp)):
            summ+=temp[i]*(10**(len(temp)-i-1))
        s2.append(summ)
        s2.append(s[j])
        temp.clear()
        summ=0

for i in range(len(temp)):
    summ+=temp[i]*(10**(len(temp)-i-1))
s2.append(summ)

summ=0

# 식의 값을 최소로 만들려면
# - 기호 뒤 숫자들을 괄호로 묶는다. (최대가 되도록)

index=0

for i in range(len(s2)):
    if s2[i]=='-':
        if index==0:
            index=1
    elif type(s2[i])==int:
        if index==0:
            summ+=s2[i]
        elif index==1:
            summ-=s2[i]

print(summ)