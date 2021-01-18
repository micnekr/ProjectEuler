import primes


if __name__ == '__main__':
    with open("primesBelow10to7.txt", "r") as f:
        text = f.readline()
        primeNums = [int(num) for num in text.split(", ")]

    # with open("primesBelow10to7.txt", "w") as f:
    #     f.seek(0)
    #
    #     print("getting primes")
    #     primeNums = primes.partialSieve(10 ** 7, primeNums)
    #     print(primeNums)
    #     print("writing primes")
    #     f.write(", ".join([str(num) for num in primeNums if num < 10 ** 7]))

    maxNum = 10 ** 7

    minRatio = -1
    minValue = -1

    for number, factorisation in primes.iterateNumberPrimes(primeNums, maxNum):
        phi = primes.smartPhi(factorisation)
        if sorted(str(number)) == sorted(str(phi)):
            # print("works")
            ratio = number/phi
            if minRatio == -1 or minRatio > ratio:
                minRatio = ratio
                minValue = number

    print("Done")
    print(minValue, minRatio)
    print(primes.factorise(minValue, primeNums))
