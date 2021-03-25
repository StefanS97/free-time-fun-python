def is_valid_walk(walk):
    if len(walk) == 10:
        a = 0
        b = 0
        for i in range(len(walk)):
            if walk[i] == 'n':
                a += 1
            if walk[i] == 's':
                a -= 1
            if walk[i] == 'w':
                b += 1
            if walk[i] == 'e':
                b -= 1
        if a-b == 0 and a+b == 0:
            return True
        else:
            return False
    else:
        return False