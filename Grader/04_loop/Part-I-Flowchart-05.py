c = input()
import math
if c ==  'S':
    m = int(input())
    q = 1
    r = 0
    t = 1
    k = 1
    n = 3
    x = 3
    i = 0
    p = ""
    while i<m:
        if (4*q)+r-t <(n*t):
            p = p+str(n)
            i = i+1
            a = 10*(r-n*t)
            n = 10*((3*q)+r)//t - 10*n
            q = 10*q
            r = a
        else:
            a = ((2*q)+r)*x
            b = ((7*k*q)+2+x*r)//(x*t)
            q = k*q
            t = x*t
            x = x+2
            k = k+1
            n = b
            r = a
    p = p[0] + '.' + p[1:]
    print('pi =', p)          
else:
    if c =='R':
        n = int(input())
        k = 0
        p = 0
        while k < n+1:
            p +=((-3)**(-k))/((2*k)+1)
            k+=1
        P = math.sqrt(12)
        p *= P
        p = round(p,12)
        print('pi =', p)   
    else:
        if c =='P':
            p = math.sqrt(7+math.sqrt(6+math.sqrt(5)))
            p = round(p,6)
            print('pi =', p)
        else:
            print('Invalid')
        
        
