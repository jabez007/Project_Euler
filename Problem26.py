#Project Euler, problem 26

def reciprocalCycles(n): #Finds remainders until they start to repeat
    longest = []
    for i in range(1,n):
        remainders = [1%i]
        index = 0
        while remainders.count((remainders[index]*10)%i)==0:
            remainders = remainders+[(remainders[index]*10)%i]
            index+=1
        if len(remainders)>len(longest):
            longest = remainders
