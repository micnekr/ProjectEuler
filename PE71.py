if __name__ == '__main__':
    # binary search our way through it
    target = 3/7
    print(target)

    maxDenum = 10 ** 6

    d = 11

    bestNumberator = -1
    bestDist = 1

    while d <= maxDenum:
        if d % 7 == 0:
            d += 1
            continue

        # get the closest two numbers to the target
        numerator = target * d
        # get the one to the left
        numerator = int(numerator)
        newFraction = numerator / d
        distance = abs(newFraction - target)
        if distance < bestDist:
            bestNumberator = numerator
            bestDist = distance

        d += 1
    print(d, bestNumberator, bestDist)
