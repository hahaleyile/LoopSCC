def start(x, y, det):
    while x > 0:
        x = x - 1
        if det:
            y = y + 1
        else:
            while y > 0:
                y = y - 1
