def longDivision(num):
    current = "1"
    result = ""
    decimal = False
    states = []
    while True:
        if int(current)<num:
            result+="0"
            if not decimal:
                result+="."
                decimal=True
            current+="0"
            continue
        remainder = int(current)%num
        result+=str(int((int(current)-remainder)/num))
        current=str(remainder)
        current+="0"
        state = [result[-1], remainder]
        if state in states:
            cyclesCounter = len(states)-states.index(state)
            return cyclesCounter
        else:
            states.append(state)
        if remainder==0:
            return -1

if __name__ == '__main__':
    maxNum = 0
    maxCycles = 0
    for i in range(1, 1000):
        cycles = longDivision(i)
        if cycles>maxCycles:
            maxCycles = cycles
            maxNum = i
    print(maxNum)
