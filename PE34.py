def factorial(num):
    total = 1
    for i in range(1, num+1):
        total*=i
    return total

def digFac(num):
    num = str(num)
    sum=0
    for ch in num:
        sum+=factorial(int(ch))
    return sum

def checkFac(num):
    if len(str(num))==1:
        return False
    return num==digFac(num)


if __name__ == '__main__':
    counter = 1
    sum = 0
    while True:
        if checkFac(counter):
            sum+=counter
            print(sum)
        counter+=1
