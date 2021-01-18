from primes import sieveGen

primes = []

generator = sieveGen(primes)

print(next(generator))
print(primes)

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getAllNeededPrimesForDigits(digitNum):
    maxNum = 10 ** digitNum
    while primes[-1] * primes[-1] < maxNum:
        next(generator)


def isPrimeReduced(number):
    if number > primes[-1] * primes[-1]:
        raise ValueError("The primes are too small to check if this number is a prime")
    for prime in primes:
        if number % prime == 0:
            return False
    return True


def findNewNumbers(string, lastIndex, filler, left):
    if left == 0:
        return [string]
    if lastIndex == len(string):
        return []
    out = []
    for i in range(lastIndex, len(string)):
        newString = string[:i] + filler + string[i + 1:]

        newStrings = findNewNumbers(newString, i + 1, filler, left - 1)
        out += newStrings
    return out

def replaceWithNumbers(string, isAtBegining):
    try:
        int(string)
        return [string]
    except:
        digitsString = None
        if isAtBegining:
            digitsString = "123456789"
        else:
            digitsString = "0123456789"
        out = []
        #find the first letter
        for i in range(len(string)):
            if string[i] in alphabet:
                for j in digitsString:
                    newWord = list(string)
                    newWord[i] = j
                    out += replaceWithNumbers("".join(newWord), False)
                break
        return out

getAllNeededPrimesForDigits(2)

print(primes)

print(isPrimeReduced(38))

currentLength = 4

print(replaceWithNumbers("A2B", True))

# *2*3*3
# *4*6*9

#answer is 121313

getAllNeededPrimesForDigits(6)
for i in "0123456789":
    newString = "*2*3*3".replace("*", i)
    print(isPrimeReduced(int(newString)), newString)

dictionary = {}

while True:

    getAllNeededPrimesForDigits(currentLength)

    for fillerNumber in range(2, currentLength):
        for fillerDigit in "0123456789":
            stringsToCheck = findNewNumbers(alphabet[:currentLength], 0, fillerDigit, fillerNumber)
            # print(fillerNumber, fillerDigit, stringsToCheck)

            # check every string
            for repeatedDigitString in stringsToCheck:
                templatePrimeCount = 0
                #replace every letter with a number
                numbersToCheck = replaceWithNumbers(repeatedDigitString, True)
                for numberToCheck in numbersToCheck:
                    if isPrimeReduced(int(numberToCheck)):
                        templateString = []
                        for i in range(len(numberToCheck)):
                            if repeatedDigitString[i] in "0123456789":
                                templateString.append("*")
                            else:
                                templateString.append(numberToCheck[i])
                        dictIndexString = "".join(templateString)
                        if dictIndexString not in dictionary:
                            dictionary[dictIndexString] = 1
                        else:
                            dictionary[dictIndexString] += 1
                            if dictionary[dictIndexString] == 8:
                                print("done")
                                print(dictIndexString)


    currentLength += 1
