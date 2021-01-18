def checkLetters(str1, str2):
    letters = {}
    for letter in str1:
        if letter not in letters:
            letters[letter] = 1
        else:
            letters[letter] += 1
    for letter in str2:
        if letter not in letters:
            return False
        else:
            letters[letter] -= 1

    for value in letters.values():
        if value != 0:
            return False
    return True


print(checkLetters("12344", "43412"))

counter = 1

while True:
    newString = "1" + str(counter)

    newNum = int(newString)

    hasWorked = True
    for multiplier in [2, 3, 4, 5, 6]:
        if not checkLetters(newString, str(newNum * multiplier)):
            hasWorked = False
            break

    if hasWorked:
        print(newString)
        break

    counter += 1