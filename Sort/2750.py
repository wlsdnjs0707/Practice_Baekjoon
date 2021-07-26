# 수 정렬하기
# 시간복잡도 = O(n**2)

a=[]

n = int(input())

for i in range(n):
    a.append(int(input()))

# O(n**2)의 시간복잡도를 갖는 정렬
# 버블정렬, 선택정렬, 삽입정렬

# Case 1 (버블정렬)
def bubble(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

# Case 2 (선택정렬)
def selection(a):
    for i in range(len(a)):
        min_index=i
        for j in range(i+1,len(a)):
            if a[min_index]>a[j]:
                min_index=j
        
        temp=a[min_index]
        a[min_index]=a[i]
        a[i]=temp

# Case 3 (삽입정렬)
def insertion(a):
    for i in range(1,len(a)):
        for j in range(i,0,-1):
            if a[j]<a[j-1]:
                temp=a[j]
                a[j]=a[j-1]
                a[j-1]=temp

s = int(input())

if s==1:
    bubble(a)
    print(a)
elif s==2:
    selection(a)
    print(a)
elif s==3:
    insertion(a)
    print(a)