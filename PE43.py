def lexicographic(input):
    input = list(input)
    while True:
        i = 0
        for x in range(1, len(input)):
            if input[x-1]<input[x]:
                if x>i:
                    i=x

        if i==0:
            break

        j = 0
        for x in range(0, len(input)):
            if input[i-1]<input[x]:
                if x>j:
                    j=x

        input[i-1], input[j]=input[j], input[i-1]
        input[i:]=input[len(input) - 1 : i - 1 : -1]

        yield input

def substringDivisiblePal(num):
    num = str(num)
    divisibilities=[2, 3, 5, 7, 11, 13, 17]
    for i in range(7):
        if int(num[i+1:i+4])%divisibilities[i]!=0:
            return False
    return True

if __name__ == '__main__':
    sum = 0
    lex = lexicographic("0123456789")
    num = 123456789
    while int(num)<9876543211:
        if substringDivisiblePal(num):
            sum+=int(num)
            print(num, sum)
        num = "".join(next(lex))
    print(sum)
