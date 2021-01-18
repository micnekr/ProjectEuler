import primes

def isPandigital(num):
    num = str(num)
    digitsNum = len(num)
    digits=[]
    for ch in num:
        if ch in digits:
            return False
        digits.append(ch)
    for ch in digits:
        if not 0<int(ch)<=digitsNum:
            return False
    return True


if __name__ == '__main__':
    gen = primes.sieveGen()
    num=next(gen)
    while num<987654322:
        if isPandigital(num):
            print(num)
        num = next(gen)
