import primes as pr

if __name__ == '__main__':
    primes = [2]
    gen = pr.sieveGen()
    next(gen)
    bestSettings = [0, 0]
    bestScore = 0
    for a in range(-999, 1000):
        print(a)
        for b in range(-1000, 1001):
            score = 0
            for n in range(120):
                num = n**2 + a*n + b
                if num<0:
                    continue
                while num>primes[-1]:
                    primes.append(next(gen))
                if num in primes:
                    score+=1
                else:
                    break
            if score>bestScore :
                bestScore=score
                bestSettings = [a, b]
                print(bestScore)

    print(bestSettings, bestScore)
