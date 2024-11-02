def start(x0, det):
    x = x0
    while x < 100:
        x = x + 1
        while x < 100:
            if det:
                break
            x = x + 1
