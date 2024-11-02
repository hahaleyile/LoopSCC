def start(x, i):
    while i < 100:
        if x > 5:
            x -= 2
            i += 3
        elif x < -5:
            x += 3
            i += 5
        else:
            x += 2
            i += 7
