def dig_pow(n, p):
    nstring = str(n)
    nlist = list(nstring)
    phelper = 0

    for i in range(len(nlist)):
        phelper += int(nlist[i])**p
        p+=1

    if (phelper % n) == 0:
        return int(phelper/n)
    if (phelper % n) != 0:
        return -1