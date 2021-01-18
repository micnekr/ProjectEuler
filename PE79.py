def record(value, map):
    if value not in map:
        map[value] = 1
    else:
        map[value] += 1

if __name__ == '__main__':
    with open("p079_keylog.txt", "r") as f:
        lines = f.readlines()

    firstDigits = {}
    secondDigits = {}
    thirdDigits = {}
    for line in lines:
        line = line[:-1]

        record(line[0], firstDigits)
        record(line[1], secondDigits)
        record(line[2], thirdDigits)

    print(firstDigits)
    print(secondDigits)
    print(thirdDigits)

    print("first digit:")
    for firstDigit in firstDigits:
        if firstDigit not in secondDigits:
            print(firstDigit)

    print("last digits:")

    for thirdDigit in thirdDigits:
        if thirdDigit not in secondDigits:
            print(thirdDigit)

    for passcodeLength in range(2, 10):
        possibleNums = "0123456789"

        nums = ["0"] * passcodeLength

        while nums != ["9"] * passcodeLength:
            for i in range(len(nums) - 1, -1, -1):
                nums[i] = str(int(nums[i]) + 1)
                if int(nums[i]) == len(possibleNums):
                    nums[i] = "0"
                else:
                    break

            # check the passcode
            works = True
            numsToTry = ["7"] + nums + ["0"]
            for login in lines:
                try:
                    firstIndex = numsToTry.index(login[0])
                    secondIndex = numsToTry[firstIndex + 1:].index(login[1])
                    thirdIndex = numsToTry[secondIndex + 1:].index(login[2])
                except ValueError:
                    works = False
                    break
            if works:
                print("".join(numsToTry))

        print(passcodeLength)
