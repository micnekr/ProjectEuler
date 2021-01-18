import math

def triangular():
    counter = 1
    previous = 0
    while True:
        previous+=counter
        yield previous
        counter+=1

def factorsNum(num):
    factors = 0

    for i in range(1, math.ceil(math.sqrt(num))):
        if num%i==0:
            factors+=2
    return factors

if __name__ == '__main__':
    gen = triangular()
    num = factors = 0
    while factors<=500:
        num = next(gen)
        factors = factorsNum(num)
    print(num, factors)
