def searcher(num, starting, ending, numberToLookFor, lengthLeft):

    num = str(num)
    numberToLookFor = str(numberToLookFor)

    if lengthLeft <= 0:
        if num == numberToLookFor:
            return [[num]]
        else:
            return False

    out = []
    lastDigits = num[2:]

    if lastDigits in starting:
        for newNumber in starting[lastDigits]:
            result = searcher(newNumber[0], starting, ending, numberToLookFor, lengthLeft - 1)
            if result != False:
                for resultOption in result:
                    if num not in resultOption:
                        out.append([num] + resultOption)
                    elif lengthLeft == 6:
                        out.append(resultOption)
    return out


def genTriangle(n):
    return n * (n+1) // 2


def genSquare(n):
    return n * n


def genPent(n):
    return n * (3 * n - 1) // 2


def getHex(n):
    return n * (2 * n - 1)


def getHept(n):
    return n * (5 * n - 3) // 2


def getOct(n):
    return n * (3 * n - 2)


def getTypes(n, allLists):
    types = []
    for i in range(len(allLists)):
        if int(n) in allLists[i]:
            types.append(i + 3)
    return types


def genAll(min, max, function):
    list = []
    n = 1
    while True:
        term = function(n)

        if term > max:
            break

        if term >= min:
            list.append(term)

        n += 1
    return list


if __name__ == '__main__':

    minNum = 10 ** 3
    maxNum = 10 ** 4 - 1

    # all the numbers
    triangleNums = genAll(minNum, maxNum, genTriangle)
    sqNums = genAll(minNum, maxNum, genSquare)
    pentNums = genAll(minNum, maxNum, genPent)
    hexNums = genAll(minNum, maxNum, getHex)
    heptNums = genAll(minNum, maxNum, getHept)
    octNums = genAll(minNum, maxNum, getOct)

    allLists = [triangleNums, sqNums, pentNums, hexNums, heptNums, octNums]

    starting = {}
    ending = {}

    for i in range(len(allLists)):
        base = i + 3
        currentList = allLists[i]
        for number in currentList:
            number = str(number)

            firstTwoDigits = number[:2]
            lastTwoDigits = number[2:]

            if firstTwoDigits not in starting:
                starting[firstTwoDigits] = [[number, base]]
            else:
                starting[firstTwoDigits].append([number, base])

            if lastTwoDigits not in ending:
                ending[lastTwoDigits] = [[number, base]]
            else:
                ending[lastTwoDigits].append([number, base])

    print(ending)

    results = []

    for triangleNum in triangleNums:
        result = searcher(triangleNum, starting, ending, triangleNum, 6)
        if result:
            for resultSet in result:
                if resultSet not in results:
                    results.append(resultSet)
    print("results", results)

    for result in results:
        roughTypes = []
        types = []

        for number in result:
            currentTypes = getTypes(number, allLists)

            # if type in types:
            #     isWorking = False
            #     break

            types.append(currentTypes)

            for type in currentTypes:
                if type not in roughTypes:
                    roughTypes.append(type)

        if len(roughTypes) == 6:
            print(result, roughTypes, types)
            # only ['5625', '2512', '1281', '8128', '2882', '8256']  seems to work
            # sum is 28684

    # now, let the pain begin

    # get cycles of 4
    # cycles = []
    # encountered = []

    # queue = []
    #
    # for i in range(len(allLists)):
    #     currentList = allLists[i]
    #     for number in currentList:
    #         if number not in queue:
    #             queue.append([number])

    # print(queue, len(queue))
    # while len(queue) > 0:
    #     currentItem = queue.pop(0)
    #     if currentItem[0] in encountered:
    #         continue
    #
    #     encountered.append(currentItem[0])
    #
    #     if len(currentItem[1]) == 3:
    #         print(currentItem)
    #         break
    #
    #     currentNum = str(currentItem[0])
    #
    #     firstDigits = currentNum[:2]
    #     lastDigits = currentNum[2:]
    #
    #     startingList = starting[firstDigits]
    #     endingList = ending[lastDigits]
    #     print(startingList)
    #     print(endingList)
    #     break

    # for number in queue:
    #     number = str(number)
    #
    #     firstDigits = number[:2]
    #     lastDigits = number[2:]
    #
    #     # time the cycles
    #     initNumber = number
    #     numberOfTurns = 0
    #     while True:
    #         print(number)
    #         if number == initNumber:
    #             break
    #         numberOfTurns += 1
    #
    #     print(numberOfTurns)
    #     break
