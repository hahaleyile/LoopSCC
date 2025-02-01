def start(t, x, y):
    while t > 0:
        if x == y + 1:
            y += 2
        else:
            x += 2
        t -= 1
