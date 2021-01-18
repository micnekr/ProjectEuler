import primes as pr
import math

if __name__ == '__main__':
    primes = [2]
    gen = pr.sieveGen()
    next(gen)
    number = 1
    while True:
        while primes[-1]<number:
            primes.append(next(gen))
        if number not in primes:
            possible = False
            for prime in primes:
                if number>prime:
                    sqrt = math.sqrt((number-prime)/2)
                    if sqrt==int(sqrt):
                        possible=True
                        break
            if not possible:
                print(number)
        number+=2
