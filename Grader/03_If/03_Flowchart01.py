A,B,C,D = input().split()
a = int(A)
b = int(B)
c = int(C)
d = int(D)
if a>b:
    a,b = b,a
    if d>=a:
        if c>d:
            c = c-a
    else:
        c = c+a
    b = a+c+d
else:
    if c>a>=b:
        d = d+a
    if d>c:
        b = b+2
    else:
        b = 2*b
          
print(a,b,c,d)