if __name__ == '__main__':

    memTable = {}

    hits = 0

    for i in range(2, 10**7):

        if i % 1000 == 0:
            print(i)

        memoryList = [i]

        wasMemorised = False
        # transform
        while i != 1 and i != 89:

            if i in memTable:
                wasMemorised = True
                break

            digits = list(str(i))

            result = 0
            for digit in digits:
                result += int(digit) ** 2

            i = result

            memoryList.append(i)

        if wasMemorised:
            target = memTable[i]
        else:
            target = i

        if target == 89:
            hits += 1

        for memorisedValue in memoryList:
            memTable[memorisedValue] = target

    print(hits)
