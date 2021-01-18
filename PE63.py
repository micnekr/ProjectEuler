counter = 1
maxNum = 100
power = 1

number = 0

while True:
    for i in range(1, maxNum):
        if len(str(counter**power))==power:
            number+=1
            print(counter, power)
        counter+=1
    counter=1
    power+=1
    print(number)
