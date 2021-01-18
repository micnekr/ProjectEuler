if __name__ == '__main__':
    result = 1
    maxNum = 10 ** 11
    for i in range(7830457):
        result *= 2
        if result > maxNum:
            result %= maxNum
    print(str(28433 * result + 1))