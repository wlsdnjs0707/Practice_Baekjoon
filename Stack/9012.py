# 괄호

t = int(input())

for i in range(t):

    s = list(input())
    check=[]
    switch=0

    for i in s:
        if i=='(':
            check.append('(')
        elif i==')':
            try:
                check.pop()
            except IndexError:
                switch=1
                break
        
    if len(check)==0 and switch==0:
        print('YES')
    else:
        print('NO')