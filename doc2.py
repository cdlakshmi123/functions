def max(a,b,c):
    if a>b and b>c:
        return a
    elif b>c and c>a:
        return b
    elif c>a and a>b:
        return c
print(max(40,30,60))