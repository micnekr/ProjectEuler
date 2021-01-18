import math


def getPeriod(num):
    sqrt = math.sqrt(num)
    wholePart = int(sqrt)

    # double inverted part = sqrt - wholePart
    denominator = num - wholePart ** 2
    wholeNumeratorPart = wholePart
    print(denominator, wholeNumeratorPart)


if __name__ == '__main__':
    print(getPeriod(23))
