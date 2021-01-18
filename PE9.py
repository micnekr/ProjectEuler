def isPythagorean(a, b, c):
    return a**2+b**2==c**2

def findPyth(max):
    for a in range(1, max-1):
        for b in range(1, max-a):
            c = max-a-b
            if isPythagorean(a, b, c):
                return [a, b, c]

if __name__ == '__main__':
    max = 1000

    ans = findPyth(max)
    print(ans[0]*ans[1]*ans[2])
