def start(x, i):
    while i < 100:
        if x > 1:
            x += 1
            i += 3
        elif x < -1:
            x += 1
            i += 5
        else:
            x += 1
            i += 7
