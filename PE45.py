def trGen():
    seed = 1
    while True:
        yield int(seed*(seed+1)/2)
        seed+=1

def peGen():
    seed = 1
    while True:
        yield int(seed*(3*seed-1)/2)
        seed+=1

def heGen():
    seed = 1
    while True:
        yield seed*(2*seed-1)
        seed+=1

if __name__ == '__main__':
    trgen = trGen()
    pegen = peGen()
    hegen = heGen()
    trs = [next(trgen)]
    pes = [next(pegen)]
    hes = [next(hegen)]
    while True:
        num = next(trgen)
        trs.append(num)
        while pes[-1]<num:
            pes.append(next(pegen))
        while hes[-1]<num:
            hes.append(next(hegen))
        if num in pes and num in hes:
            print(num)
