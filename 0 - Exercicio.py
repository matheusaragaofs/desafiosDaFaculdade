def prod (a,b):
    if b>1:
        print(a+a)
        prod(a,b-1)
prod(7,2)