import primes as pr

gen = pr.sieveGen()
primes = [2]
num = next(gen)
sum = 0
for i in range(4):
    num = next(gen)
    primes.append(num)
while True:
    numStr = str(num)
    truncatable = True
    while len(numStr)>1 and truncatable:
        numStr = numStr[1:]
        if int(numStr) not in primes:
            truncatable=False
    numStr=str(num)
    while len(numStr)>1 and truncatable:
        numStr = numStr[:-1]
        if int(numStr) not in primes:
            truncatable=False
    if truncatable:
        sum+=num
        print(num, sum)
    primes.append(num)
    num = next(gen)
