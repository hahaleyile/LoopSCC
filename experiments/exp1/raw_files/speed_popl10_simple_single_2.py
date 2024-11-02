def start(x0, y0):
    x = x0
    y = y0

    while True:
        if x < 100:
            x = x + 1
            y = y + 1
        elif y < 30:
            x = x + 1
            y = y + 1
        else:
            break
