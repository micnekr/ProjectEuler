import primes as pr

def arePermutations(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    if len(num1)!=len(num2):
        return False
    for ch in num1:
        num1 = num1[1:]
        index = num2.find(ch)
        if index==-1:
            return False
        num2 = num2[:index]+num2[index+1:]
    return True
if __name__ == '__main__':
    gen = pr.sieveGen()
    primes = []
    num = next(gen)
    while num<1000:
        num = next(gen)
    while num<10000:
        primes.append(num)
        num = next(gen)
    permutations = []
    for prime in primes:
        isNew = True
        for classified in permutations:
            if arePermutations(prime, classified[0]):
                isNew = False
                classified.append(prime)
                break
        if isNew:
            permutations.append([prime])


    for classified in permutations:
        if len(classified)<3:
            continue
        numberOfDiffs = 0
        for index1 in range(len(classified)):
            num1 = classified[index1]
            for index2 in range(index1+1, len(classified)):
                num2 = classified[index2]
                difference = num2-num1
                if difference==3330:
                    numberOfDiffs+=1
        if numberOfDiffs==2:
            print(classified)
