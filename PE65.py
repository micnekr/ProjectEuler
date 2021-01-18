import math

if __name__ == '__main__':
    numbers = [2, 1, 2]
    for i in range(34):
        numbers += [1, 1]
        numbers.append(2 * i + 4)

    maxNum = 100

    numbers = numbers[:maxNum]

    numbers = numbers[::-1]

    print(numbers)

    result = 1/numbers.pop(0) + numbers.pop(0)
    print(result)
    while len(numbers) != 0:
        result = numbers.pop(0) + 1/result
    print(result)

    denominator = 1
    while True:
        newResult = result * denominator
        if math.fabs(int(newResult) - newResult) < 0.0000001:
            break
        denominator += 1
    print(newResult) # 29

