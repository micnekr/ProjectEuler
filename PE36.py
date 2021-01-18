def decToBin(dec):
    out = ""
    while dec>0:
        remainder = dec%2
        dec = int((dec-remainder)/2)
        out = str(remainder)+out
    return out

def isPalindrome(num):
    num = str(num)
    for i in range(int(len(num)/2)):
        if num[i]!=num[-(i+1)]:
            return False
    return True

if __name__ == '__main__':
    max = 1000000
    sum = 0
    for i in range(1, max):
        if isPalindrome(i):
            if isPalindrome(decToBin(i)):
                sum+=i
    print(sum)
