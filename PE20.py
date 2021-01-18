def factorial(num):
    total=1
    for i in range(1, num):
        total*=i
    return total

def addDigs(num):
    total = 0
    num = str(num)
    for dig in num:
        total+=int(dig)
    return total

if __name__ == '__main__':
    print(addDigs(factorial(100)))
