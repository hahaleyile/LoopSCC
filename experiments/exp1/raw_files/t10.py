def start(x, y, det):
    while x > y:
        if det:
            y = y + 1
        else:
            x = x - 1
