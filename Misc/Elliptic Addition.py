def EA([x1, y1], [x2, y2]):
    if x1==x2 and y1==y2:
        b=input("b=? ")
        m=(3*x1**2 + b)/(2*y1)
    else:
        m=(y2-y1)/(x2-x1)
