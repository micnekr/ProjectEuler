def genSpiral(max):
    current = 1
    step = 2
    rotations = 0
    sum = 1
    while True:
        if rotations==4:
            rotations=0
            step+=2
        current+=step
        rotations+=1
        if current>max:
            return sum
        print(current)
        sum+=current

if __name__ == '__main__':
    print(genSpiral(1001**2))
