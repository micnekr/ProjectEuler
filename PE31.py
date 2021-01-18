def sumAll(currency, steps):
    sum = 0
    for i in range(len(currency)):
        sum+=currency[i]*steps[i]
    return sum

def count(currency, steps):
    nextDig = True
    for i in range(len(currency)):
        if nextDig:
            currency[i]+=1
        else:
            return
        sum = sumAll(currency, steps)
        if sum>200:
            currency[i]=0
            nextDig=True
        else:
            nextDig=False

if __name__ == '__main__':
    # +0ne £2 way and 2*1£
    ways = 1
    max = 2
    steps = [1, 2, 5, 10, 20, 50, 100]
    currency = [0, 0, 0, 0, 0, 0, 0]
    while currency[-1]<2:
        result = sumAll(currency, steps)
        if result==200:
            ways+=1
        count(currency, steps)
    print(ways)
