def pentagonal(seed):
    return int(seed*(seed*3-1)/2)

def pentagonalGen():
    count = 1
    while True:
        yield pentagonal(count)
        count+=1

def getPent(counter, pents, gen):
    while counter>=len(pents):
        pents.append(next(gen))
    return pents[counter]

if __name__ == '__main__':
    gen = pentagonalGen()
    pentagonalNums = []
    best = 100000000000000000000000
    bestPair = []
    counter = 0
    num = 1
    while True:
        num = getPent(counter, pentagonalNums, gen)
        for prevInd in range(counter):
            previous = pentagonalNums[prevInd]
            if num-previous in pentagonalNums:
                while pentagonalNums[-1]<num+previous:
                    pentagonalNums.append(next(gen))
                if num+previous in pentagonalNums:
                    print(num+previous)
                    if num-previous<best:
                        best = num-previous
                        bestPair = [previous, num]
                        print(best)
        counter+=1
