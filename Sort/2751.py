# 수 정렬하기 2
# 시간복잡도 = O(nlogn)
# 시간복잡도가 O(nlogn)인 정렬 알고리즘 : 퀵정렬,병합정렬,힙정렬

a = []

n = int(input())

for i in range(n):
    a.append(int(input()))

def merge_sort(a):

    def sort(low,high):
        if high-low<2:
            return
        
        mid = (low+high)//2
        sort(low,mid)
        sort(mid,high)
        merge(low,mid,high)

    def merge(low,mid,high):
        temp = []
        l=low
        h=mid

        while l<mid and h<high:
            if a[l]<a[h]:
                temp.append(a[l])
                l+=1
            else:
                temp.append(a[h])
                h+=1
        
        while l<mid:
            temp.append(a[l])
            l+=1

        while h<high:
            temp.append(a[h])
            h+=1

        for i in range(low,high):
            a[i]=temp[i-low]

    return sort(0,len(a))

merge_sort(a)
print(a)