import math

def isPandigital(num):
    avaliable="123456789"
    num=str(num)
    if len(num)!=9:
        return False
    digits = ""
    for dig in num:
        if (dig in digits) or dig not in avaliable:
            return False
        digits += dig
    return True

if __name__ == '__main__':
    max = 987654321

    max = int(math.sqrt(max))+1
    nums = []
    for a in range(1, max):
        max2 = int(max/a)+1
        for b in range(1, max2):
            multiple = a*b
            if multiple not in nums:
                pandigital = str(a)+str(b)+str(multiple)
                if isPandigital(pandigital):
                    nums.append(multiple)
                    print(a, b)
                    print(multiple)

    sum = 0
    for num in nums:
        sum += num

    print(sum)
