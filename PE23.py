import math, factors

def isAbundant(num):
    fNum = factors.factorsSum(num)
    return fNum>num

if __name__ == '__main__':
    max = 28123

    abundant = []

    for toTest in range(max+1):
        if isAbundant(toTest):
            abundant.append(toTest)

    print(abundant)

    sum = 0
    for toTest in range(1, max+1):
        isImpossible = True
        for j in abundant:
            num = toTest-j
            if j>(toTest/2)+1:
                break
            if num in abundant:
                isImpossible=False
                break
        if isImpossible:
            sum+=toTest
            print(toTest/max)

    print(sum)
