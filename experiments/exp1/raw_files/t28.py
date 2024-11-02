def start(x, y):
    while x > y:
        x = x - 1
        x = x + 1000
        y = y + 1000
    while y > 0:
        y = y - 1
    while x < 0:
        x = x + 1