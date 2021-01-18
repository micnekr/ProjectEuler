import factors as fc

def uniqueFactorise(factors):
    uniqueFactors = []
    for factor in factors:
        if factor not in uniqueFactors:
            #print(factor)
            uniqueFactors.append(factor)
    return uniqueFactors

def getUniqueFactors(num):
    return uniqueFactorise(fc.factorize(num))

if __name__ == '__main__':
    number = 1
    consequitive = 4
    while True:
        nums = []
        for i in range(consequitive):
            nums.append(number+i)
        factors = []
        suitable=True
        count = 0
        for num in nums:
            factorGroup = getUniqueFactors(num)
            factors.append(factorGroup)
            if len(factorGroup)<consequitive:
                suitable = False
                break
            count+=1
        if suitable:
            print(number)
            break
        number+=1+count
