import math

from collections import deque

def sieve(maxNum):
    maxNum += 1
    numbers = [True] * (maxNum // 2)
    primes = [2]

    for i in range(1, maxNum // 2):
        if numbers[i]:
            primes.append(2 * i + 1)
            for j in range(3 * i + 1, maxNum // 2, 2 * i + 1):
                numbers[j] = False
    return primes


def isPrime(num, primes):
    if num <= 1:
        return False
    if num > primes[-1] ** 2:
        raise ValueError("Not enough primes for number " + str(num) + " and last prime " + str(primes[-1]))
    for prime in primes:
        if num < prime ** 2:
            return True
        if num % prime == 0:
            return False
    return True


def partialSieve(maxNum, partialPrimes=None):
    if partialPrimes is None:
        step = int(math.sqrt(maxNum)) + 2
        partialPrimes = sieve(step)
    else:
        step = partialPrimes[-1] + 1

    for lastNum in range(step, maxNum, step):
        sieveArray = [True] * (step // 2)

        for prime in partialPrimes:
            if prime == 2:
                continue

            # get the smallest divisible number greater than the minimum

            smallestNum = (lastNum // prime + 1) * prime

            # if it is even, add the prime once more to make it odd
            if smallestNum % 2 == 0:
                smallestNum += prime

            for i in range(smallestNum, lastNum + step, 2 * prime):
                # print("i - lastNum", i - lastNum)
                index = (i - lastNum) // 2

                sieveArray[index] = False

        for newPrimeIndex in range(len(sieveArray)):
            if sieveArray[newPrimeIndex]:
                partialPrimes.append(lastNum + 2 * newPrimeIndex + 1)

    return partialPrimes


def factorise(num, primes):
    if num == 1:
        return []

    for prime in primes:
        if num % prime == 0:
            return [prime] + factorise(num // prime, primes)
    return False


def iterateNumberPrimes(primeNums, maxNum):
    stack = deque()
    lastIndex = -1
    for i in range(len(primeNums)):
        if primeNums[i] < maxNum:
            lastIndex = i
            prime = primeNums[i]
            stack.append((i, prime, [prime]))
    while len(stack) != 0:
        primeIndex, currentNum, primeFactorisation = stack.popleft()
        for nextPrimeIndex in range(primeIndex, lastIndex + 1):
            nextPrime = primeNums[nextPrimeIndex]
            # print("primes", primeNums[primeIndex], primeNums[nextPrimeIndex])
            newNum = currentNum * nextPrime
            # print("newNum", newNum)
            if newNum >= maxNum:
                break
            stack.append((nextPrimeIndex, newNum, primeFactorisation + [nextPrime]))
        yield currentNum, primeFactorisation


def smartPhi(factorisation):
    primesDistributions = {}
    for prime in factorisation:
        if prime not in primesDistributions:
            primesDistributions[prime] = 1
        else:
            primesDistributions[prime] += 1
    result = 1
    for key, value in primesDistributions.items():
        result *= key ** (value - 1) * (key - 1)
    return result


if __name__ == '__main__':
    print(smartPhi([2, 2, 3]))

    import time

    startTime = time.time()
    primes = partialSieve(10 ** 5)

    print(primes)
    print(len(primes))


    print("time: ", time.time() - startTime)

    nums = []
    for nextNum, factorisation in iterateNumberPrimes(primes, 10 ** 5):
        nums.append(nextNum)
        print(nextNum, factorisation)
    print(nums)
    print(sorted(nums) == [i for i in range(2, 10 ** 5)])
    print()
