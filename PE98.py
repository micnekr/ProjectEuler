# def generateRandomMappings(length):
#     out = []
#     availableNumbers = "0123456789"
#
#     # first number
#     for i in availableNumbers[1:]:
#         out.append([i])
#
#     for currentLength in range(1, length):
#         newElements = []
#         for element in out:
#             for newNum in availableNumbers:
#                 newElements.append(element + [newNum])
#         out = newElements
#     return out
import math


def isInt(num):
    return num == int(num)

def transformQuote(string, sendMapping=False):
    digitMappings = {}

    lastChOrd = ord("A")

    newString = ""
    for ch in string:
        if ch not in digitMappings:
            digitMappings[ch] = chr(lastChOrd)
            newString += chr(lastChOrd)
            lastChOrd += 1
        else:
            newString += digitMappings[ch]
    if sendMapping:
        return newString, digitMappings
    else:
        return newString


def isInt(num):
    return num == math.floor(num)

# 18769
if __name__ == '__main__':
    with open("p098_words.txt", "r") as f:
        words = f.readline().split(",")

    for wordIndex in range(len(words)):
        words[wordIndex] = words[wordIndex].replace("\"", "")

    stringToSorted = {}

    cases = {}

    for word in words:
        stringToSorted[word] = sorted(word)

    for word in words:
        thisSorted = stringToSorted[word]
        for otherWord in words:
            if word == otherWord:
                break
            if stringToSorted[otherWord] != thisSorted:
                continue
            if otherWord in cases:  # the family has been considered already
                break
            if word not in cases:
                cases[word] = [otherWord]
            else:
                cases[word].append(otherWord)

    longestWord = ""
    for word in cases.keys():
        if len(word) > len(longestWord):
            longestWord = word

    maxNum = 10 ** len(longestWord) - 1

    squares = {}
    for i in range(int(math.sqrt(maxNum)), 0, -1):
        string = str(i ** 2)
        # loop through the digits

        newString = transformQuote(string)
        if newString not in squares:
            squares[newString] = [i * i]
        else:
            squares[newString].append(i * i)

    print(squares)

    # go through the cases:

    highest = 0

    for case in cases.keys():
        listOfOthers = cases[case]
        sortedValue = stringToSorted[case]

        # do the same thing
        simplifiedCase, mappings = transformQuote(case, True)
        possibleSquares = squares[simplifiedCase]

        # transform the second one
        secondString = ""
        for ch in listOfOthers[0]:
            secondString += mappings[ch]

        # go over all the possible square values
        for possibleSquare in possibleSquares:
            squareString = str(possibleSquare)

            # create a digit mapping
            digitMapping = {}
            for i in range(len(squareString)):
                digitMapping[simplifiedCase[i]] = squareString[i]

            # get the new number
            newNumberString = ""
            for ch in secondString:
                newNumberString += digitMapping[ch]
            if newNumberString[0] != "0" and isInt(math.sqrt(int(newNumberString))):
                # check if greater

                print(int(newNumberString), possibleSquare)

                if int(newNumberString) > highest:
                    highest = int(newNumberString)
                if possibleSquare > highest:
                    highest = possibleSquare
    print(highest)

    # highest = 0

    # for case in cases.keys():
    #     listOfOthers = cases[case]
    #     sortedValue = stringToSorted[case]
    #
    #     # random mappings
    #
    #     allWordsWorked = True
    #
    #     highestOfSquares = 0
    #     for wordToCheck in [case] + listOfOthers:
    #
    #         isSquare = False
    #
    #         for i in range(10 ** (len(wordToCheck) - 1), 10 ** (len(wordToCheck)))[::-1]:  # could be more efficient
    #
    #             iStr = str(i)
    #
    #             mapping = {}
    #             usedNumbers = []
    #
    #             isSuitable = True
    #
    #             # check if it can be considered a number that works for the situation
    #             for chIndex in range(len(wordToCheck)):
    #                 currentCh = wordToCheck[chIndex]
    #                 if iStr[chIndex] in usedNumbers:
    #                     isSuitable = False
    #                     break
    #                 elif currentCh not in mapping:
    #                     mapping[currentCh] = iStr[chIndex]
    #                     usedNumbers.append(iStr[chIndex])
    #                 elif mapping[currentCh] != iStr[chIndex]:
    #                     isSuitable = False
    #                     break
    #
    #             # check if it is a root
    #             if isSuitable and isInt(math.sqrt(i)):
    #                 isSquare = True
    #                 if i > highestOfSquares:
    #                     highestOfSquares = i
    #                 break
    #         if not isSquare:
    #             allWordsWorked = False
    #             break
    #     if allWordsWorked and highestOfSquares > highest:
    #         highest = highestOfSquares
    #         print(highest)
    # print(highest)
