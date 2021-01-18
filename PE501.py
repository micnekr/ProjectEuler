import primes
import os.path


def numberOfFactorsNaive(num):
    occurrences = 0
    for i in range(1, num + 1):
        if num % i == 0:
            occurrences += 1
    return occurrences


# def get8FactorsNumbers(maxNum, primeNums):
#     nums = 0
#     for num1Index in range(len(primeNums)):
#         hasMadeAnAddition = False
#
#         num1 = primeNums[num1Index]
#
#         # a ** 7
#         if num1 ** 7 > maxNum:
#             hasMadeAnAddition = True
#             nums += 1
#
#         # a ** 3 * b
#         # num1cubed = num1 ** 3
#         # for num2Index in range(0, num1Index):
#         #     num2 = primeNums[num2Index]
#         #     if num1cubed * num2 > maxNum:
#         #         break
#         #     nums += 2  # a ** 3 * b and b ** 3 * a
#         #     hasMadeAnAddition = True
#
#         # a * b * c
#         # TOD: small values, e.g. 2
#         # nums += (num1Index - 1) * (num1Index - 2)
#
#         if not hasMadeAnAddition:
#             return nums
#     return nums

def get8FactorsNumbers(maxNum, primeNums):
    numOfWays = 0
    for num1Index in range(len(primeNums)):
        possibility1 = primeNums[num1Index] ** 3


# TODO: divide 10 ** 12 number by a prime, use other primes to check if it is prime


if __name__ == '__main__':

    primeNums = []

    if os.path.isfile("primesBelow10to6.txt"):
        with open("primesBelow10to6.txt", "r") as f:
            text = f.readline()
            primeNums = [int(num) for num in text.split(", ")]
    else:
        with open("primesBelow10to6.txt", "w") as f:
            f.seek(0)

            print("getting primes")
            primeNums = primes.partialSieve(10 ** 6)
            print(primeNums)
            print("writing primes")
            f.write(", ".join([str(num) for num in primeNums]))

    print(primeNums)

    # print(primes.factorise(10, primeNums))
    # print(primes.factorise(180, primeNums))
    # print(primes.factorise(224427, primeNums))

    # occurrences = 0
    # for i in range(1, 10000):
    #     if numberOfFactorsNaive(i) == 8:
    #         print(primes.factorise(i, primeNums))
    #         occurrences += 1
    # print(occurrences)

    print(get8FactorsNumbers(100, primeNums))

    # a a a b
    # a b c
    # a ^ 7
