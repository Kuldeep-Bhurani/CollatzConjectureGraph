def Algo(n):
    lst = [n]
    while True:
        if n % 2 == 0:
            m = int(n/2)
            n = m
            lst.append(m)
        elif n == 1:
            break
        else:
            m = int(n*3+1)
            n = m
            lst.append(m)
    return lst
