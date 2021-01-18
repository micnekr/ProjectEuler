import primes as pr

if __name__ == '__main__':
    max = 1000000
    primes = []
    gen = pr.sieveGen()
    num = 0

    bestScore = 0
    bestPrime = 0

    while True:
        num = next(gen)
        if num>=max:
            break
        primes.append(num)

    lastPrime = primes[-1]

    while True:
        try:
            start = primes[0]
        except:
            break

        print(start, max)

        if start>int(max/2):
            break

        sum = start

        for index in range(1, len(primes)):

            prime = primes[index]
            sum+=prime

            if sum>max:
                break

            if sum in primes:
                if index+1 >= bestScore:
                    bestScore = index+1
                    bestPrime = sum

        primes = primes[1:]

    print(bestScore, bestPrime)
