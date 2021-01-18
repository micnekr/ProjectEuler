def fibonacci():
    a = b = 1
    yield a
    yield b
    while True:
        a,b = a+b,a
        yield a

if __name__ == '__main__':
    gen = fibonacci()
    sum = 0
    while True:
        num = next(gen)
        if num>4000000:
            print(sum)
            break
        if num%2==0:
            sum+=num
