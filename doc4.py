def list(a):
    i=0
    while i<len(a):
        c=""
        j=-1
        while j>=-len(a[i]):
            c=c+a[i][j]
            j=j-1
        i=i+1
    print(c)
list(["1234abcd"])