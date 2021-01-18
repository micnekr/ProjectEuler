import itertools
import math

import primes


def isReversiblePrime(nums, map):
    for num1 in nums:
        for num2 in nums:
            if num1 != num2:
                if not num1 in map[num2]:
                    return False
    return True


if __name__ == '__main__':
    with open("primesBelow10to6.txt", "r") as f:
        text = f.readline()
        millionPrimes = [int(num) for num in text.split(", ")]

    numOfPrimes = 10 ** 4
    primeNums = primes.partialSieve(numOfPrimes)
    print(primeNums)

    # find the ones that work
    # primeSplits = {}
    #
    # reversePrimeSplits = {}

    memorisedPairs = {}

    doubleWorkingPrimePairs = []

    # squareRoot = int(math.sqrt(numOfPrimes)) + 1

    for left in primeNums:
        print(left / primeNums[-1])
        for right in primeNums:
            left, right = str(left), str(right)

            # print(primeStr, left, right)
            # check if both can be split
            if primes.isPrime(int(right + left), millionPrimes) and primes.isPrime(int(left + right), millionPrimes):

                prime1, prime2 = int(left), int(right)
                minPrime, maxPrime = min(prime1, prime2), max(prime1, prime2)

                if (minPrime, maxPrime) not in memorisedPairs:
                    memorisedPairs[(minPrime, maxPrime)] = 1
                    doubleWorkingPrimePairs.append((minPrime, maxPrime))

    # for prime in primeNums:
    #     primeStr = str(prime)
    #
    #     if primeStr[0] > primeStr[-1]:
    #         continue
    #
    #     # if prime > squareRoot:
    #     #     break
    #
    #     # all possible ways to split it
    #     for i in range(1, len(primeStr)):
    #         left = primeStr[:i]
    #         right = primeStr[i:]
    #
    #         if left[0] == "0" or right[0] == "0":
    #             continue
    #
    #         # print(primeStr, left, right)
    #         # check if both can be split
    #         if primes.isPrime(int(left), primeNums) and primes.isPrime(int(right), primeNums):
    #
    #             prime1, prime2 = int(left), int(right)
    #             minPrime, maxPrime = min(prime1, prime2), max(prime1, prime2)
    #
    #             if (minPrime, maxPrime) not in memorisedPairs and primes.isPrime(int(right + left), primeNums):
    #                 memorisedPairs[(minPrime, maxPrime)] = 1
    #                 doubleWorkingPrimePairs.append((minPrime, maxPrime))
    #
    #             # if prime not in primeSplits:
    #             #     primeSplits[prime] = [[int(left), int(right)]]
    #             # else:
    #             #     primeSplits[prime].append([int(left), int(right)])
    #             # prime1, prime2 = int(left), int(right)
    #             # minPrime, maxPrime = min(prime1, prime2), max(prime1, prime2)
    #             #
    #             # if minPrime not in reversePrimeSplits:
    #             #     reversePrimeSplits[minPrime] = [maxPrime]
    #             # else:
    #             #     otherPrimes = reversePrimeSplits[minPrime]
    #             #     if maxPrime not in otherPrimes:
    #             #         otherPrimes.append(maxPrime)
    #             #     else:
    #             #         doubleWorkingPrimePairs.append([minPrime, maxPrime])

    print("Done first step")
    print(doubleWorkingPrimePairs)

    doubleWorkingNumbersMap = {}
    for pair in doubleWorkingPrimePairs:
        num1 = pair[0]
        num2 = pair[1]

        if num1 not in doubleWorkingNumbersMap:
            doubleWorkingNumbersMap[num1] = [num2]
        else:
            doubleWorkingNumbersMap[num1].append(num2)
        if num2 not in doubleWorkingNumbersMap:
            doubleWorkingNumbersMap[num2] = [num1]
        else:
            doubleWorkingNumbersMap[num2].append(num1)

    primesToChooseFrom = doubleWorkingNumbersMap.keys()

    print(doubleWorkingNumbersMap)
    print("Done preprocessing")

    for startPrime in primesToChooseFrom:
        others = doubleWorkingNumbersMap[startPrime]
        # print(others)

        # select 4
        for i in range(len(others)):
            for j in range(i + 1, len(others)):
                if not isReversiblePrime([others[i], others[j]], doubleWorkingNumbersMap):
                    continue
                for k in range(j + 1, len(others)):
                    if not isReversiblePrime([others[i], others[j], others[k]], doubleWorkingNumbersMap):
                        continue
                    for l in range(k + 1, len(others)):
                        if isReversiblePrime([others[i], others[j], others[k], others[l]], doubleWorkingNumbersMap):
                            print(startPrime, others[i], others[j], others[k], others[l])

    # choose 5 primes
    # minIndex = 1
    # maxIndex = 400
    # indexNum = 5
    #
    # print(primeNums[maxIndex])
    #
    # indices = [i for i in range(minIndex, maxIndex)][:indexNum]
    # indices[-1] -= 1  # so that the first loop resets it
    #
    # iteration = 0
    # while True:
    #
    #     iteration += 1
    #
    #     # if the first one is as big as it can be and the rest are increasing, stop
    #     if indices[0] >= maxIndex - len(indices):
    #         isAllIncreasing = True
    #         for i in range(1, len(indices)):
    #             if indices == [4, 5, 6, 7, 8]:
    #                 if indices[i] - indices[i - 1] != 1:
    #                     isAllIncreasing = False
    #                     break
    #         if isAllIncreasing:
    #             break
    #
    #     # count up
    #     for i in range(len(indices) - 1, -1, -1):
    #         newNum = indices[i] + 1
    #         if newNum == maxIndex:
    #             indices[i] = 0
    #         else:
    #             indices[i] = newNum
    #             break
    #
    #     # make sure that it all increases
    #
    #     lastNum = -1
    #
    #     isLegitimate = True
    #
    #     for i in range(len(indices)):
    #
    #         if indices[i] <= lastNum:
    #             if lastNum >= maxIndex:
    #                 isLegitimate = False
    #             indices[i] = min(lastNum, maxIndex - 1)
    #             lastNum += 1
    #         else:
    #             lastNum = indices[i] + 1
    #
    #     if isLegitimate:
    #         chosenPrimes = [primeNums[index] for index in indices]
    #
    #         if iteration % 100000 == 0:
    #             print(indices)
    #
    #         # try all the possibilities
    #         isWorking = True
    #         for prime1 in chosenPrimes:
    #             for prime2 in chosenPrimes:
    #                 if prime1 == prime2:
    #                     continue
    #                 # print(primes.isPrime(int(str(prime1) + str(prime2)), primeNums), int(str(prime1) + str(prime2)))
    #                 if not primes.isPrime(int(str(prime1) + str(prime2)), primeNums):
    #                     isWorking = False
    #                     break
    #             if not isWorking:
    #                 break
    #         if isWorking:
    #             print(chosenPrimes)
    #             break
