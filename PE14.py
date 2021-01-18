#837799
endWith = 1000000

sequences = {}
bestSteps = 0
best = 0
for i in range(1, endWith):
    cur = i
    steps = 0
    while True:
        if cur==1:
            break;
        if cur in sequences:
            steps+=sequences[cur]
            break;
        if cur%2==0:
            cur = int(cur/2)
        else:
            cur = 3*cur+1
        steps+=1
    sequences[i] = steps
    if steps>bestSteps:
        bestSteps = steps
        best = i
print(best)
