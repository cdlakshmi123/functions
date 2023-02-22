def even(a):
    i=0
    c=[]
    # even=0
    while i<len(a):
        if a[i]%2==0:
            # even=even+a[i]
            c.append(a[i])
        i=i+1
    print("even is ",c)
even([1,2,3,4,5,6,7,8,9])