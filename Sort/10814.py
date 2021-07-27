# 나이순 정렬

n = int(input())

s = []

for i in range(n):
    age,name=input().split()
    s.append([int(age),name])

for i in range(len(s)):
    for j in range(i,0,-1):
        if s[j][0]<s[j-1][0]:
            s[j],s[j-1]=s[j-1],s[j]

for i in range(len(s)):
    print("{0} {1}".format(s[i][0],s[i][1]))
