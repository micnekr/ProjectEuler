import primes, math

num = 600851475143

gen = primes.sieveGen()
max = math.sqrt(num)

mult = 1

while True:
    current = next(gen)
    if num%current==0:
        print(current)
        mult*=current
    if current>max:
        break
print(mult/71)
