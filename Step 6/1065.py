# 한수

def arithmetic(n:int):

    count = 0
    switch = 1

    for i in range(1,n+1):
        switch=1
        temp = list(map(int,list(str(i))))
        temp2 = []
        if len(temp)<=2:
            count+=1
        else:
            for j in range(len(temp)-1):
                if j!=len(temp):
                    temp2.append(temp[j+1]-temp[j])
            for k in range(len(temp2)-1):
                if k!=len(temp2):
                    if temp2[k]!=temp2[k+1]:
                        switch=0
            if switch==1:
                count+=1

    print(count)

n = int(input())

arithmetic(n)