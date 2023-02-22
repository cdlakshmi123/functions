def list(a):
    i=0
    
    while i<len(a):
        cu=0
        cl=0
        j=0
        while j<len(a[i]):
            if a[i][j].isupper():
                cu=cu+1
            if a[i][j].islower():
                cl=cl+1
            j=j+1
        i=i+1
    print(cu)
    print(cl)
list(["The Dog Name is Kutty"])

