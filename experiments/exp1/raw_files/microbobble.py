def start(t, b):
    flag = 1
    while t > 0:
        if flag == 1:
            b -= 1
            flag = 0
        elif flag == 0:
            b += 1
            flag = 1
        else:
            pass
        t -= 1
