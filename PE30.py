def getPow(num, exp):
    num = str(num)
    sum = 0
    for dig in num:
        sum+=int(dig)**exp
    return sum

def checkExp(num, exp):
    if len(str(num))==1:
        return False
    return num==getPow(num, exp)


if __name__ == '__main__':
    exp = 5

    sum=0

    count = 2
    while True:
        if checkExp(count, exp):
            sum+=count
            print(sum)
        count+=1
