# 절댓값 힙
# 최소힙, 절댓값 기준

heap = []

def insert(h,v):

    h.append(v)

    index = len(h)-1

    while index>=0:
        if (h[index])*-1==h[index//2]: #절댓값이 같을때 음수의 우선순위가 먼저
            if h[index]<h[index//2]:
                h[index],h[index//2]=h[index//2],h[index]
            index=index//2
        else:
            if abs(h[index])<abs(h[index//2]): #절댓값이 작은수의 우선순위가 먼저
                h[index],h[index//2]=h[index//2],h[index]
                index=index//2
            else:
                break

def pop(h):

    if len(h)==0:
        print(0)
    elif len(h)==1 or len(h)==2:
        print(h.pop(0))
    elif len(h)==3:
        print(h[0])
        h[0]=h.pop()
        if h[0]*-1==h[1]:
            if h[0]>h[1]:
                h[0],h[1]=h[1],h[0]
        elif abs(h[0])>abs(h[1]):
            h[0],h[1]=h[1],h[0]
    else:
        print(h[0])
        h[0]=h.pop()
        index=0

        while index<len(h):
            if index==0:
                if abs(h[index])<abs(h[1]) and abs(h[index])<abs(h[2]):
                    # 우선순위를 바꾸지 않아도 될경우
                    break
                else:
                    if abs(h[1])<=abs(h[2]):
                        h[index],h[1]=h[1],h[index]
                        index=1
                    else:
                        h[index],h[2]=h[2],h[index]
                        index=2
            else:
                if index*2+1<len(h):
                    if abs(h[index])<abs(h[index*2]) and abs(h[index])<abs(h[index*2+1]):
                        # 우선순위를 바꾸지 않아도 될경우
                        break
                    else:
                        if abs(h[index*2])<=abs(h[index*2+1]):
                            h[index],h[index*2]=h[index*2],h[index]
                            index=index*2
                        else:
                            h[index],h[index*2+1]=h[index*2+1],h[index]
                            index=index*2+1
                else:
                    break

n = int(input())

for i in range(n):
    c = int(input())

    if c==0:
        pop(heap)
    else:
        insert(heap,c)