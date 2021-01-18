def minPath(x, y, rows, side, table={}):

    if x == y == side - 1:
        return rows[x][y]

    if (x, y) in table:
        return table[(x, y)]

    option = None
    if x < side - 1:
        option = minPath(x + 1, y, rows, side, table)
    if y < side - 1:
        yOption = minPath(x, y + 1, rows, side, table)
        if option is None:
            option = yOption
        else:
            option = min(option, yOption)

    option += rows[x][y]

    table[(x, y)] = option
    return option

if __name__ == '__main__':
    with open("p081_matrix.txt", "r") as f:
        lines = f.readlines()

    rows = []

    for line in lines:
        line = [int(i) for i in line.replace("\n", "").split(",")]
        rows.append(line)

    side = 80

    print(minPath(0, 0, rows, side))