import math


def isPalindrome(num):
    num = str(num)
    firstHalf = num[:len(num) // 2]
    secondHalf = num[math.ceil(len(num) / 2):]

    return firstHalf == secondHalf[::-1]

if __name__ == '__main__':
    counter = 0
    for i in range(10 ** 4):

        numberWorks = False
        # the tries
        for j in range(50):
            i += int(str(i)[::-1])
            if isPalindrome(i):
                numberWorks = True
                break
        if not numberWorks:
            counter += 1
    print(counter)
