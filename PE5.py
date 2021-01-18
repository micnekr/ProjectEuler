import factorisation as fts
divs = 20

num = 1
for i in range(1, divs+1):
    if num%i!=0:
        print(i)
        factors = fts.factorize(i)
        newN = num
        for factor in factors:
            if newN%factor==0:
                newN = int(newN/factor)
        num = newN*i
print(num)
