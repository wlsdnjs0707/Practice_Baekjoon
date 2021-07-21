# Fly me to the Alpha Centauri

t = int(input()) # test case

for e in range(t):
    x,y = map(int,input().split())

    m = y-x

    i=0
    while m>0:
        if m<=i:
            count+=1
            break
        m = m-i*2
        count=i*2
        i+=1

    print(count)