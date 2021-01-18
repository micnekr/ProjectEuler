for a in range(10,100):
    for b in range(a+1, 100):
        for mult in range(2, 10):
            if str(mult) in str(a) and str(mult) in str(b) and "0" not in str(a) and "0" not in str(b):
                #print(a, b)
                for ch1 in range(len(str(a))):
                    for ch2 in range(len(str(b))):
                        if str(a)[1-ch1]==str(mult) and str(b)[1-ch2]==str(mult):
                            #print(int(str(a)[ch1])/int(str(b)[ch2]), a/b)
                            if a/b==int(str(a)[ch1])/int(str(b)[ch2]):
                                print(a, b, mult)
