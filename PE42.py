import os

import math

def isTr(number):
    n = math.floor(math.sqrt(number*2))
    return number*2==n*(n+1)



name = "p042_words.txt"

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

wObj = open(name)
wordsStr = wObj.read()
wObj.close()

# get all words in an array
words = []

currentWord = ""
readingWord = False;

for ch in wordsStr:
     if ch == "\"":
         if readingWord:
             words.append(currentWord)
             currentWord = ""
         readingWord = not readingWord
     elif readingWord:
         currentWord+=ch

num = 0
for word in words:
    summ = 0
    for ch in word:
        place = ALPHABET.find(ch)+1
        if place != -1:
            summ+=place
    if(isTr(summ)):
        num+=1
print(num)
