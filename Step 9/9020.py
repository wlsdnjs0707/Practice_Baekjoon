# 골드바흐의 추측

t = int(input()) # Test case

for i in range(t):
    n = int(input())

    d=[]
    ans=[]
    check=0

    for i in range(1,n):
        if i==1:
            check=1
        else:
            for j in range(2,i):
                if i%j==0:
                    check=1
        if check==0:
            d.append(i)
        check=0

    for i in range(len(d)):
        for j in range(len(d)):
            if d[i]+d[j]==n:
                ans.append([d[i],d[j]])

    for i in range(int(len(ans)/2)):
        ans.pop()

    small = n
    s = 0

    for i in range(len(ans)):
        if small>ans[i][1]-ans[i][0]:
            small=ans[i][1]-ans[i][0]
            s=i

    print("{0} {1}".format(ans[s][0],ans[s][1]))