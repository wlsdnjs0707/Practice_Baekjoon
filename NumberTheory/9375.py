# 패션왕 신해빈

t = int(input()) # test case

for _ in range(t):

    n = int(input())
    c = []
    index=[]
    seq=[]

    for i in range(n):
        c.append(list(input().split()))
        index.append(0)
        seq.append(0)

    for i in range(n):
        if index[i]==0:
            index[i]=1
            seq[i]+=1
        for j in range(n):
            if c[i][1]==c[j][1] and index[j]==0:
                index[j]=1
                seq[i]+=1
    
    # 모든경우의수 -1 (전부안입는경우 1가지)
    # (옷의수+1)*(옷의수+1)* ... -1

    answer = 1

    for i in range(len(seq)):
        if seq[i]!=0:
            answer=answer*(seq[i]+1)

    print(answer-1)