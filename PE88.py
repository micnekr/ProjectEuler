import primes

def findMinNumber(k, factorisations, factorisationsByNumberOfFactors):
    for numberOf1s in range(k - 1, -1, -1):
        numberOfOtherFactors = k - numberOf1s

        try:
            numbersWithSuitableFactors = factorisationsByNumberOfFactors[numberOfOtherFactors]
            print(numberOf1s)
        except KeyError:
            continue


if __name__ == '__main__':
    with open("primesBelow10to6.txt", "r") as f:
        text = f.readline()
        primeNums = [int(num) for num in text.split(", ")]

    numberOfNumbersToCalculate = 10 ** 5

    numDivisors = []

    for i in range(2, numberOfNumbersToCalculate):
        numDivisors.append(primes.factorise(i, primeNums))
        if i % 10000 == 0:
            print(i)

    factorisationsByNumberOfFactors = {}
    for divisorsIndex in range(len(numDivisors)):
        divisors = numDivisors[divisorsIndex]
        number = divisorsIndex + 2

        numOfDivisors = len(divisors)

        if numOfDivisors not in factorisationsByNumberOfFactors:
            factorisationsByNumberOfFactors[numOfDivisors] = [number]
        else:
            factorisationsByNumberOfFactors[numOfDivisors].append(number)

    print(factorisationsByNumberOfFactors)


    print("factorisations found")
    findMinNumber(100, numDivisors, factorisationsByNumberOfFactors)

