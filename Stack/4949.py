# 균형잡힌 세상

while True:
    s = list(input().split())

    if s[0]=='.':
        break

    check1=[]
    check2=[]
    switch=0
    
    for j in s:
        c=list(str(j))
        for i in range(len(c)):
            if c[i]=='(':
                check1.append(0)
            elif c[i]==')':
                try:
                    check1.pop()
                except IndexError:
                    switch=1
            elif c[i]=='[':
                check2.append(0)
            elif c[i]==']':
                try:
                    check2.pop()
                except IndexError:
                    switch=1
    
    if switch==0 and len(check1)==0 and len(check2)==0:
        print('yes')
    else:
        print('no')