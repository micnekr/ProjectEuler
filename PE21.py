import math

def factorsSum(num):
    sum = 0

    for i in range(1, math.ceil(math.sqrt(num))):
        if num%i==0:
            sum+=i
            sum+=int(num/i)
    return sum-num

def isAmicable(num):
    sum = factorsSum(num)
    return num==factorsSum(sum) and sum!=num

if __name__ == '__main__':
    sum = 0
    for i in range(2, 10000+1):
        if isAmicable(i):
            sum+=i
    print(sum)
