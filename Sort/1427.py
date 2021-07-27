# 소트인사이드

n = list(map(int,str(input())))

for i in range(len(n)):
    for j in range(i,len(n)):
        if n[i]<n[j]:
            temp=n[i]
            n[i]=n[j]
            n[j]=temp

for i in n:
    print("{0}".format(i),end='')