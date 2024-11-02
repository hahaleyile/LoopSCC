def start(x, y):
    while x > y:
        x = x - y - 1
        z = 100 + 2 * y
        while z > 0:
            z = z - 1
