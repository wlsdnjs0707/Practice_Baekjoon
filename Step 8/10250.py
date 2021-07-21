# ACM 호텔

t = int(input()) # Test Case

hor=1
ver=0

for i in range(t):
    h,w,n = map(int,input().split()) # h=층, w=너비, n=손님

    if n>h:
        hor += n//h
        ver += n%h
    else:
        hor=1
        ver=n

    print("{0}{1:0>2}".format(ver,hor))

    hor=1
    ver=0