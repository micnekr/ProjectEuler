def factorial(num, table={}):
    if num in table:
        return table[num]
    if num <= 1:
        return 1
    else:
        out = factorial(num - 1, table) * num
        table[num] = out
    return out


if __name__ == '__main__':

    counter = 0

    for i in range(3, 10 ** 6):
        if i % 1000 == 0:
            print(i)

        numberOfTerms = 2

        numberHistory = []

        while True:

            if i in numberHistory:
                break

            numberHistory.append(i)

            iStr = str(i)

            i = 0
            for digit in list(iStr):
                i += factorial(int(digit))

            numberOfTerms += 1

        if len(numberHistory) == 60:
            counter += 1
    print(counter)
