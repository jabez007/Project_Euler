def xgcd(a, b):
    if a%b==0:
        return [0, 1]
    else:
        [x, y] = xgcd(b, a%b)
        return [y, x-(y*(a/b))]

print xgcd(8, 12)
