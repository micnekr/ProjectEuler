import primes

if __name__ == '__main__':
    with open("primesBelow10to7.txt", "r") as f:
        text = f.readline()
        primeNums = [int(num) for num in text.split(", ")]

    sumOfNums = 0
    for number, factors in primes.iterateNumberPrimes(primeNums, 10 ** 6 + 1):
        sumOfNums += primes.smartPhi(factors)
    print(sumOfNums)
