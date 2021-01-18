import primes as ps

def rotate(num):
    num = str(num)
    out = ""
    for i in range(1, len(num)):
        out+=num[i]
    out+=num[0]
    return out

def isCircularPrime(input, primes, gen):
    length = len(str(input))
    for i in range(length):
        num = input
        for j in range(i):
            num = rotate(num)
        num = int(num)
        try:
            prime = primes[-1]
        except:
            prime=0
        while num>=prime:
            prime = next(gen)
            primes.append(prime)
        if num not in primes:
            return False
    return True


if __name__ == '__main__':
    max = 1000000
    # max=100
    primes = []
    gen = ps.sieveGen()
    num = 0
    numberOfPrimes = 0
    counter = 0
    while num<max:
        while len(primes)<=counter:
            num = next(gen)
            primes.append(num)
        num = primes[counter]
        if isCircularPrime(num, primes, gen) and num<max:
            print(num)
            numberOfPrimes+=1
        counter+=1
    print(numberOfPrimes)
