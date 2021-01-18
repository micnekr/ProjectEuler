def getSlope(x1, y1, x2, y2):
    if x2 == x1:
        return "nan"
    return (y2-y1) / (x2 - x1)


def isRight(x1, y1, x2, y2):
    slopes = [getSlope(0, 0, x1, y1), getSlope(0, 0, x2, y2), getSlope(x1, y1, x2, y2)]

    if (x1 == x2 and y1 == y2) or (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
        return False

    for i in range(3):
        for j in range(i, 3):
            slope1 = slopes[i]
            slope2 = slopes[j]

            if isinstance(slope1, str):
                if slope2 == 0:
                    return True
            elif isinstance(slope2, str):
                if slope1 == 0:
                    return True
            elif slope1 * slope2 == -1:
                return True
    return False


if __name__ == '__main__':

    maxDims = 50

    tries = 0

    points = {}

    for x1 in range(maxDims + 1):
        print(x1)
        for y1 in range(maxDims + 1):
            points[(x1, y1)] = {}
            for x2 in range(maxDims + 1):
                for y2 in range(maxDims + 1):

                    if (x2, y2) in points[(x1, y1)] or ((x2, y2) in points and  (x1, y1) in points[(x2, y2)]):
                        continue

                    points[(x1, y1)][(x2, y2)] = 1
                    if (x2, y2) not in points:
                        points[(x2, y2)] = {
                            (x1, y1): 1
                        }
                    else:
                        points[(x2, y2)][(x1, y1)] = 1
                    if isRight(x1, y1, x2, y2):
                        # print(x1, y1, x2, y2)
                        tries += 1

    print(tries)
