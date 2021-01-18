def count(step, num, table={}):
    if (step, num) in table:
        return table[(step, num)]

    if num == 0:
        return 1

    overallCount = 0
    for newNum in range(step, num + 1):
        overallCount += count(newNum, num - newNum, table)
        # trace.append(step)
    table[(step, num)] = overallCount
    return overallCount

if __name__ == '__main__':
    maxNum = 100

    # toAdd = [0] * maxNum
    # toAdd[0] = maxNum

    print(count(1, maxNum) - 1)  # includes maxNum
