# 괄호

t = int(input())

for i in range(t):

    vps = list(input())

    s = []
    switch=0

    for i in range(len(vps)):
        if vps[i]=='(':
            s.append(vps[i])
        elif vps[i]==')':
            try:
                s.pop()
            except IndexError:
                switch=1
        
    if len(s)==0 and switch==0:
        print('YES')
    else:
        print('NO')