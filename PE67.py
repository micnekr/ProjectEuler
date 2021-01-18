def maxTotal(layer, index, table):
    if (layer, index) in table:
        return table[(layer, index)]
    currentNum = int(rows[layer][index])

    if layer == len(rows) - 1:
        return currentNum
    else:
        sum1, sum2 = maxTotal(layer + 1, index, table), maxTotal(layer + 1, index + 1, table)
        sum = max(sum1, sum2) + currentNum
        table[(layer, index)] = sum
        print(sum, (layer, index), currentNum)
        return sum


if __name__ == '__main__':
    with open("p067_triangle.txt", "r") as f:
        lines = f.readlines()
    rows = []

    for line in lines:
        line = line.replace("\n", "")
        line = line.split(" ")
        rows.append(line)
        print(line)

    # rows = [
    #     [3],
    #     [7, 4],
    #     [2, 4, 6],
    #     [8, 5, 9, 3]
    # ]

    table = {}
    print(maxTotal(0, 0, table))

