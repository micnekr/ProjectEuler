def isPal(num):
    num = str(num)
    start = 0
    end = len(num)-1
    while start<end:
        if num[start]!=num[end]:
            return False
        start+=1
        end-=1
    return True

if __name__ == '__main__':
    best = 0
    nums = []
    for a in range(1000):
        for b in range(1000):
            num = a*b
            if isPal(num):
                if num>best:
                    best=num
                    nums = [a, b]
    print(best, nums)
