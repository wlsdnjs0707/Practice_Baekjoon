# 크로아티아 알파벳

s = list(input())

count = 0
switch = 0

for i in range(len(s)):

    if switch==0:
        if i!=len(s):
            if s[i]=='c' and s[i+1]=='=':
                count+=1
                switch=1
            elif s[i]=='c' and s[i+1]=='-':
                count+=1
                switch=1
            elif s[i]=='d' and s[i+1]=='-':
                count+=1
                switch=1
            elif s[i]=='l' and s[i+1]=='j':
                count+=1
                switch=1
            elif s[i]=='n' and s[i+1]=='j':
                count+=1
                switch=1
            elif s[i]=='s' and s[i+1]=='=':
                count+=1
                switch=1
            elif s[i]=='z' and s[i+1]=='=':
                count+=1
                switch=1
            elif i<len(s)-1 and s[i]=='d' and s[i+1]=='z' and s[i+2]=='=':
                count+=1
                switch=2
            else:
                count+=1
    elif switch!=0:
        switch-=1

print(count)