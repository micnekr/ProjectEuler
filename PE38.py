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
    counter = 0
    maxPand = 0
    while len(str(counter))<5:
        pandigital = ""
        n = 1
        while len(pandigital)<9:
            pandigital+=str(n*counter)
            n+=1
        if len(pandigital)==9:
            if int(pandigital)>maxPand:
                if isPandigital(pandigital):
                    maxPand=int(pandigital)
                    print(pandigital)
        counter+=1
