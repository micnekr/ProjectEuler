import primes

if __name__ == '__main__':
    with open("primesBelow10to6.txt", "r") as f:
        text = f.readline()
        primeNums = [int(num) for num in text.split(", ")]

    # primeNums = primes.partialSieve(10**7, primeNums)
    print(primeNums)

    number = 1

    currentStep = 2

    lastTry = currentStep

    numberOfTries = 0

    numOfPrimes = 0
    numberOfComposites = 1

    while True:

        numberOfTries += 1
        number += currentStep

        # check if it is a prime
        if primes.isPrime(number, primeNums):
            numOfPrimes += 1
        else:
            numberOfComposites += 1

        # print(number, numberOfTries, numOfPrimes, numOfPrimes + numberOfComposites)

        if numberOfTries % 4 == 0:
            currentStep += 2
            print(numOfPrimes / (numOfPrimes + numberOfComposites))
            # check the ratio
            if numOfPrimes / (numOfPrimes + numberOfComposites) < 0.1:
                print(number)
                print(currentStep - 1)
                break
