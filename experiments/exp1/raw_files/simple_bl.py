def start(t):
    d = 1
    while t > 0:
        if d * d == 1:
            d = -d
        else:
            d = 5
        t -= 1
