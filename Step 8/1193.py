# 분수찾기

n = int(input())

summ=0
i=0

while summ<n:
    i+=1
    summ+=i

summ=0

for j in range(i):
    summ+=j

res = n-summ

if i%2==0:
    #분자
    up=res
    #분모
    down=i-res+1
elif i%2==1:
    #분자
    up=i-res+1
    down=res

print("{0}/{1}".format(up,down))
