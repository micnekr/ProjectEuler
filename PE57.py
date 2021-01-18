def sqrt2(numIterations):
    numerator = 2
    denomenator = 1
    for i in range(numIterations):
        numerator, denomenator=denomenator,numerator
        numerator+=2*denomenator
    numerator-=denomenator
    return (numerator,denomenator)

if __name__ == '__main__':
    num = 0
    for i in range(1001):
        fraction = sqrt2(i)
        if len(str(fraction[0])) > len(str(fraction[1])):
            num += 1
    print(num)
