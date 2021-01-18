def getDig(num):
    current = 0
    digsCovered = 0
    while digsCovered<num:
        current+=1
        digsCovered+=len(str(current))
    digsCovered-=len(str(current))
    offset = num-digsCovered
    return int(str(current)[offset-1])

if __name__ == '__main__':
    #d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
    print(getDig(1)*getDig(10)*getDig(100)*getDig(1000)*getDig(10000)*getDig(100000)*getDig(1000000))
