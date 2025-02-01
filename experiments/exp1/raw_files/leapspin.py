def start(t):
    d = 1
    while t > 0:
        if d == 1:
            d -= 2
        elif d == -1:
            d += 2
        else:
            pass
        t -= 1
