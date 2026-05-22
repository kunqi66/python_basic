a,b,c=map(int,input().split(' '))
if c>b:
    c,b=b,c
if b>a:
    a,b=b,a
if b<c:
    c,b=b,c
print(a,b,c)


