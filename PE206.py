if __name__ == '__main__':
    #form = "1_2_3_4_5_6_7_8_9"
    num = 101010102

    while True:
        num += 3
        square = num ** 2

        if num % 100000 == 0:
            print(square)

        otherDigits = str(square)[0::2]
        # print(otherDigits)
        # print(square)
        if otherDigits == "123456789":
            print(square)
            print(num * 10)
            break
