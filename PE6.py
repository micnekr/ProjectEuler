def squared(max):
    out = 0
    for i in range(1, max+1):
        out += i*i
    return out

def sumSqared(max):
    out = 0
    for i in range(1, max+1):
        out+=i
    return out*out

if __name__ == '__main__':
    nums = 100

    print(sumSqared(nums)-squared(nums))
