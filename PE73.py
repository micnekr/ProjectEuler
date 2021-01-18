import math

if __name__ == '__main__':
    # binary search our way through it
    target1 = 1/3
    target2 = 1/2

    maxDenum = 12000

    d = 11

    numsInInterval = 0

    for d in range(4, maxDenum + 1):
        numerator1 = target1 * d
        numerator2 = target2 * d

        minNum = math.ceil(numerator1)
        maxNum = int(numerator2)

        for i in range(minNum, maxNum + 1):
            if math.gcd(i, d) == 1:
                numsInInterval += 1
                # print(i, d)

    print(numsInInterval)
