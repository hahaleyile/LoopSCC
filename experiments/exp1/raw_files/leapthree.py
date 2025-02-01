def start(t):
    x = 2
    y = 1
    while t > 0:
        if x - y == 1:
            y += 2
        elif y - x == 1:
            x += 2
        else:
            pass
        t -= 1
