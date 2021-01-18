text_obj = open("names.txt", "r")
text = text_obj.read()
text_obj.close()
text = text.split("|")
text.sort()
print(text[937])

sum = 0

SYMBOLS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(len(text)):
    multiplier = i+1
    name = text[i]
    total = 0
    for ch in name:
        total += SYMBOLS.find(ch)+1
    sum+=total*multiplier
print(sum)
