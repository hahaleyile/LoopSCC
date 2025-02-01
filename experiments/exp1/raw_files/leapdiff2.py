def start(t, x, y):
    flag = 1
    while t > 0:
        if flag == 1:
            x += 2
            flag = -1
        else:
            y += 2
            flag = 1
        t -= 1
