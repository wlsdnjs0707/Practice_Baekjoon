# 가운데를 말해요

import heapq as hq

n = int(input())
left_heap=[]  # 최대힙
right_heap=[]  # 최소힙

for i in range(n):
    x = int(input())
    
    if len(left_heap)==len(right_heap):
        hq.heappush(left_heap,(-x,x))
    else:
        hq.heappush(right_heap,(x,x))
    
    # 중간값보다 작은수는 왼쪽에, 큰수는 오른쪽에 있도록
    if len(left_heap)>=1 and len(right_heap)>=1 and left_heap[0][1]>right_heap[0][1]:
        max_value=hq.heappop(left_heap)[1]
        min_value=hq.heappop(right_heap)[1]
        hq.heappush(left_heap,(-min_value,min_value))
        hq.heappush(right_heap,(max_value,max_value))

    print(left_heap,right_heap)
    print(left_heap[0][1])
