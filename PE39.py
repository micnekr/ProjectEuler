
#840 has 16 variants
import math

def isTriangle(a, b, c):
    return a*a+b*b==c*c

end = 1000

bestTr = 0
best = 0
for i in range(end+1):
    print(i)
    p = i
    num = 0
    for j in range(1, i):
        a = j
        for l in range(1, p-a):
            b = l
            c = p-a-b
            if isTriangle(a, b, c):
                num+=1
    if num>bestTr:
        best = i
        bestTr = num
print(best)
