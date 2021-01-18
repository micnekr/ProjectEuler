import primes

if __name__ == '__main__':
    max = 10001

    gen = primes.sieveGen()
    for _ in range(max-2):
        next(gen)
    print(next(gen))
