class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        denominator = self.denominator * other.denominator
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        return Fraction(numerator, denominator)

    def __lt__(self, other):
        return self.numerator / self.denominator < other.numerator / other.denominator

    def __gt__(self, other):
        return self.numerator / self.denominator > other.numerator / other.denominator


# n = 40000
#
# maxSolutions = 0
#
# while True:
#     nextFraction = Fraction(1, n + 1)
#
#     fractionN = Fraction(1, n)
#
#     numOfSolutions = 0
#
#     x = n + 1
#     fractionX = Fraction(1, x)
#     while fractionN - fractionX < nextFraction:
#         result = fractionN - fractionX
#
#         if result > fractionX:
#             break
#
#         if result.denominator % result.numerator == 0:
#             numOfSolutions += 1
#             # print(fractionN, fractionX, result, nextFraction)
#             if numOfSolutions > 1000:
#                 print("done")
#                 print(fractionN, fractionX, result, nextFraction)
#                 from sys import exit
#                 exit()
#
#         x += 1
#         fractionX = Fraction(1, x)
#
#     fractionX = Fraction(n, x)
#
#     maxSolutions = max(maxSolutions, numOfSolutions)
#
#     print(maxSolutions, fractionN)
#
#     n += 1
#     # break


# 1/x+1/y=1/n
# n/x+n/y=1
# ny+nx=xy
# ny-xy=-nx
# y(n-x)=-nx
# -y(x-n)=-nx
# y=nx/(x-n)

n = 10
maxNumber = 0

from primes import factorise, sieve

primes = sieve(100000)


def checkNumber(n):
    numberOfHits = 0
    x = n
    while True:
        x += 1

        if (n * x) % (x - n) == 0:
            numberOfHits += 1

        if (n * x) // (x - n) < x:
            break
    return numberOfHits


# while True:
#
#     numberOfHits = checkNumber(n)
#
#     maxNumber = max(maxNumber, numberOfHits)
#     if maxNumber == numberOfHits:
#         print(factorise(n, primes))
#         print(n, maxNumber, numberOfHits)
#
#     if numberOfHits > 1000:
#         from sys import exit
#
#         print(n)
#         exit()
#
#     if n % 100 == 0:
#         pass
#
#     n += 10

primesNum = 7

primeRepetitions = [7, 5, 4, 4, 2, 2, 1]

constructedNumbers = [1]

for primeIndex in range(primesNum):
    prime = primes[primeIndex]

    for itemIndex in range(len(constructedNumbers)):
        number = constructedNumbers[0]
        del constructedNumbers[0]

        for i in range(primeRepetitions[primeIndex]):
            constructedNumbers.append(number)
            number *= prime

constructedNumbers = sorted(constructedNumbers)
# print(constructedNumbers)

maxVal = 0
for i in constructedNumbers:
    numOfWays = checkNumber(i)
    maxVal = max(maxVal, numOfWays)
    if numOfWays > 1000:
        print("done")
        print(i, numOfWays)
        break
    print(maxVal, i, numOfWays)

# number: 180180 number of ways: 1013
