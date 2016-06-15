#Project Euler, problem 33

def digitCancelingFractions():
    for n in range(10,100):
        if n%10==0:
            continue
        for d in range(10,100):
            if d%10==0 or n==d or n>d:
                continue
            for i in range(2):
                index = str(n).find(str(d)[i])
                if index!=-1:
                    if index==0:
                        newN = int(str(n)[1])
                        if i==0:
                            newD = int(str(d)[1])
                        else:
                            newD = int(str(d)[0])
                    else:
                        newN = int(str(n)[0])
                        if i==0:
                            newD = int(str(d)[1])
                        else:
                            newD = int(str(d)[0])
                    if (float(n)/d)==(float(newN)/newD):
                        print str(n)+"/"+str(d)
                        
