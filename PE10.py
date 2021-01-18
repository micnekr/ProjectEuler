import primes

max = 2000000

gen = primes.sieveGen()
sum = 0
prime = 0
while True:
    if prime>=max:
        break
    else:
        sum+=prime
        prime = next(gen)
print(sum)
