if __name__ == '__main__':
    maxDigitsSum = 0
    for a in range(2, 100):
        for b in range(2, 100):
            num = str(a ** b)
            digitsSum = 0
            for ch in num:
                digitsSum += int(ch)
            maxDigitsSum = max(maxDigitsSum, digitsSum)
    print(maxDigitsSum)
