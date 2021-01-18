import math


def factorial(n, memTable):
    if n <= 1:
        return 1
    if n in memTable:
        return memTable[n]

    factorialNum = factorial(n - 1, memTable) * n
    memTable[n] = factorialNum
    return factorialNum


def nChooseM(n, m, memTable):
    # partialFactorial1 = 1
    # for i in range(m, n + 1):
    #     partialFactorial1 *= i
    # mFactorial = factorial(m, memTable)
    # return partialFactorial1 // mFactorial

    return round(factorial(n, memTable) / factorial(m, memTable) / factorial(n - m, memTable))


if __name__ == '__main__':
    memTable = {}

    maxN = 100

    counter = 0

    for n in range(1, maxN + 1):
        # print(n)
        for m in range(1, n + 1):
            chooseResult = nChooseM(n, m, memTable)
            if chooseResult > 10 ** 6:
                counter += 1
            # if chooseResult != int(chooseResult):
            #     print(chooseResult, n, m)
            #     print(factorial(n, memTable), factorial(m, memTable), factorial(n - m, memTable))
    print(counter)

    print(nChooseM(23, 10, memTable))
