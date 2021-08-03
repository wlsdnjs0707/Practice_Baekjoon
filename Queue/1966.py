# 프린터 큐

t = int(input())

for _ in range(t):
    switch=0
    n,m = map(int,input().split())

    imp = list(map(int,input().split()))
    
    p=[]
    switch=0
    index=m
    count=0

    while True:

        if len(imp)==0:
            break

        for i in range(len(imp)):
            if imp[0]<imp[i]:
                switch=1
        
        if switch==1:
            imp.append(imp.pop(0))
            if index==0:
                index=len(imp)-1
            else:
                index-=1
        elif switch==0:
            if index==0:
                index=len(imp)-1
                p.append(imp.pop(0))
                count+=1
                break;
            else:
                index-=1
                count+=1
                p.append(imp.pop(0))
        switch=0

    print(count)