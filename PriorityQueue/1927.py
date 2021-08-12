# 최소 힙
# 1. 삽입
# 2. 삭제(출력)
# heapq 모듈 없이 구현

heap=[]

n = int(input())

def insert(h,v):
    h.append(v)
    index = len(h)-1

    while True:
        if h[index]<h[index//2]:
            h[index],h[index//2]=h[index//2],h[index] #swap
            index = index//2
        else:
            break
        if index==0:
            break

def pop(h):
    if len(h)==0:
        print(0)
    elif len(h)==1:
        print(h.pop())
    else:
        print(h[0])
        h[0]=h.pop()
        index = 0

        while index<len(h):
            if index*2+1<len(h):
                if h[index]<h[index*2] and h[index]<h[index*2+1]:
                    break
                else:
                    if h[index*2]<=h[index*2+1]:
                        h[index],h[index*2]=h[index*2],h[index]
                        index=index*2
                    else:
                        h[index],h[index*2+1]=h[index*2+1],h[index]
                        index=index*2+1
            else:
                break
for i in range(n):
    c = int(input())

    if c==0:
        pop(heap)
    else:
        insert(heap,c)