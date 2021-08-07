# 히스토그램에서 가장 큰 직사각형

while True:

    h = list(map(int,input().split()))
    
    if h[0]==0:
        break
    
    n = len(h)

    s=[]
    answer=[]

    for i in range(n):
        if i==0:
            s.append(i)
            for j in range(i+1,n):
                if h[j]>=h[i]:
                    s.append(j)
                else:
                    break
        elif i==n-1:
            for j in range(i,-1,-1):
                if h[j]>=h[i]:
                    s.append(j)
                else:
                    break  
        else:
            for j in range(i,-1,-1):
                if h[j]>=h[i]:
                    s.append(j)
                else:
                    break
            for j in range(i+1,n):
                if h[j]>=h[i]:
                    s.append(j)
                else:
                    break
        answer.append(len(s)*h[i])
        s.clear()

    print(max(answer))