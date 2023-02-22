def list(a,b):
    i=0
    c=[]
    s=[]
    while i<len(a):
        v=a[i]*a[i]
        c.append(v)
        n=b[i]*b[i]
        s.append(n)
        i=i+1
    print(c,s)
list([1,2,3,4,5],[26,27,28,29,30])
        

        