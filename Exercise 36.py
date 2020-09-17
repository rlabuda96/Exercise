def isit (x,y):
    if isinstance(x,int) and isinstance(y,int):
        print("This numbers are positive")
        return x + y
    else:
        print("Bad numbers")

print(isit(5,12.3))