import itertools

import primes
import math

def totient(num, table={}):
    return 1
    pass


def naiveTotient(num):
    counter = 1
    for i in range(2, num):
        if math.gcd(i, num) == 1:
            counter += 1
    return counter


def recursivelyCheck(num, factors, lastFactorIndex, possibleFactors, maxNum):
    if num > maxNum:
        return 0, -1

    print(factors)

    maxResult = 0
    chosen = -1
    for i in range(lastFactorIndex, len(possibleFactors)):
        otherNum = possibleFactors[i]
        result, newNum = recursivelyCheck(num * otherNum, factors + [otherNum], i, possibleFactors, maxNum)
        if result > maxResult:
            chosen = newNum
            maxResult = result
        pass

    selfNum = num / naiveTotient(num)

    if selfNum > maxResult:
        maxResult = selfNum
        chosen = num

    return maxResult, chosen



if __name__ == '__main__':
    with open("primesBelow10to6.txt", "r") as f:
        text = f.readline()
        primeNums = [int(num) for num in text.split(", ")]
    primesToUseNum = 10
    maxNum = 10 ** 6
    primesToUse = primeNums[:primesToUseNum]

    print(recursivelyCheck(1, [], 0,  primesToUse, maxNum))

    # numberOfReps = "0123456789"
    # for i in itertools.product(numberOfReps, repeat=primesToUseNum):
    #     indices = i[::-1]
    #     product = 1
    #     isGreater = False
    #     for primeIndex in range(len(primesToUse)):
    #         product *= primesToUse[primeIndex] ** int(indices[primeIndex])
    #         if product > maxNum:
    #             isGreater = True
    #             break
    #     if isGreater:
    #         continue
    #     print(product)

    # print(checkNumbers(primesToUse, primesToUseNum))

        # print(i, naiveTotient(i), primes.factorise(i, primeNums))
        # if i % 1000 == 0:
        #     print(i)
        # primes.factorise(i, primeNums)

