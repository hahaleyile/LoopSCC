def start(x, i, flag):
    while i < 100:
        if flag:
            if x > 5:
                x -= 5
                i += 3
            else:
                x += 2
                i += 7
        else:
            x -= 7
            flag = 1
