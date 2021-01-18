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

if __name__ == '__main__':
    lex = lexicographic("0123456789")
    for i in range(999999-1):
        next(lex)
    print("".join(next(lex)))
