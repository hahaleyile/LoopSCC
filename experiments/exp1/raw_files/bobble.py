def start(t, b, c):
    flag = 1
    while t > 0:
        if flag == 1:
            b += 1
            c += 1
            flag = -1
        else:
            b += 1
            c -= 1
            flag = 1
        t -= 1
