def start(x0, y0):
    x = x0
    y = y0
    while True:
        if x < 100:
            y += 1
            x += 1
        elif y > 0:
            y -= 1
        else:
            break
