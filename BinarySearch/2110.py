# 공유기 설치

n,c = map(int,input().split())

x=[]
visited=[0 for _ in range(n)]
for i in range(n):
    x.append(int(input()))

x.sort()
temp=[]
temp2=[]
answer=[]

def choose(level):
    switch=0
    if level==c:
        for i in range(len(temp)-1):
            temp2.append(abs(temp[i]-temp[i+1]))
            if temp[i]>temp[i+1]:
                switch=1
        if switch==0:
            answer.append(min(temp2))
        temp2.clear()
        switch=0
        return
    
    for i in range(n):
        if visited[i]==0:
            visited[i]=1
            temp.append(x[i])
            choose(level+1)
            visited[i]=0
            temp.pop()

choose(0)
print(max(answer))