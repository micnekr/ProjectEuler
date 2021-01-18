units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = [["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "ten"], "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def numToText(num):
    num = str(num)
    out = ""
    if len(num)==3:
        hundreds = int(num[0])
        addition = "hundred"
        out += units[hundreds-1]+addition
        toAdd = num[1:]
        if num[1]=="0":
            toAdd = num[2]
            if num[2]=="0":
                toAdd = ""
        if toAdd!="":
            out+="and"
            out += numToText(toAdd)
    elif len(num)==2:
        ten = int(num[0])
        if ten == 1:
            unts = int(num[1])
            out+=tens[0][unts-1]
        elif num[1]=="0":
            out+=tens[ten-1]
        else:
            out+= tens[ten-1]+numToText(num[1])

    else:
        unts = int(num[0])
        out = units[unts-1]
    return out

if __name__ == '__main__':
    text = ""
    print(numToText(102))
    for i in range(1, 1000):
        print(numToText(i))
        text+=numToText(i)
    text+="onethousand"
    print(len(text))
