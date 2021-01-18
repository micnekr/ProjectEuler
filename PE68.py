import itertools


def checkSum(value, sides):
    eachSum = -1
    rows = []
    for i in range(sides):
        firstValue = value[i]
        secondValueIndices = [i + sides, sides + (i + 1) % sides]
        # check first and second for sum
        currentSum = firstValue + value[secondValueIndices[0]] + value[secondValueIndices[1]]
        rows.append([firstValue, value[secondValueIndices[0]], value[secondValueIndices[1]]])
        if eachSum == -1:
            eachSum = currentSum
        elif eachSum != currentSum:
            return False, []
    return True, rows

# def checkSum(value, sides):
#     eachSum = -1
#     for i in range(sides):
#         currentSum = sum(getRow(i, value, sides))
#         print(currentSum, getRow(i, value, sides))
#         if eachSum == -1:
#             eachSum = currentSum
#         elif eachSum != currentSum:
#             return False
#     return True
#
#
# def getRow(i, value, sides):
#     firstValue = value[i]
#     secondValueIndices = [i + sides, sides + (i + 1) % sides]
#     # check first and second for sum
#     return [firstValue] + secondValueIndices

if __name__ == '__main__':

    sides = 5

    figures = []

    for possibleValue in itertools.permutations([i for i in range(1, sides * 2 + 1)]):
        outerNumbers = possibleValue[:sides]

        firstValue = outerNumbers[0]
        isFirstLowest = True
        for otherValue in outerNumbers:
            if otherValue < firstValue:
                isFirstLowest = False
                break

        if isFirstLowest:
            success, rows = checkSum(possibleValue, sides)
            if success:
                figures.append([possibleValue, rows])

    print(figures)  # [[(1, 2, 3, 5, 6, 4), [[1, 5, 6], [2, 6, 4], [3, 4, 5]]], [(1, 3, 2, 6, 5, 4), [[1, 6, 5], [3, 5, 4], [2, 4, 6]]], [(1, 3, 5, 4, 6, 2), [[1, 4, 6], [3, 6, 2], [5, 2, 4]]], [(1, 5, 3, 6, 4, 2), [[1, 6, 4], [5, 4, 2], [3, 2, 6]]], [(2, 4, 6, 3, 5, 1), [[2, 3, 5], [4, 5, 1], [6, 1, 3]]], [(2, 6, 4, 5, 3, 1), [[2, 5, 3], [6, 3, 1], [4, 1, 5]]], [(4, 5, 6, 2, 3, 1), [[4, 2, 3], [5, 3, 1], [6, 1, 2]]], [(4, 6, 5, 3, 2, 1), [[4, 3, 2], [6, 2, 1], [5, 1, 3]]]]

    representations = []
    for figure in figures:
        representation = ""
        for triplet in figure[1]:
            representation += str(triplet[0]) + str(triplet[1]) + str(triplet[2])
        print(figure[1], representation)
        if len(representation) == 16:
            representations.append(representation)
    print(representations)

    # print(checkSum([4, 6, 5, 2, 3, 1], sides))
