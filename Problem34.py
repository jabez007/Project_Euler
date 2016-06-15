#Project Euler, problem 34

factorials=[1,1,2,6,24,120,720,5040,40320,362880]

def digitFactorials():
    total = 0
    for n in range(10,2540161):
        #start at 10 because we need at least two digits for a sum
        #end at 2540160 because =9!*7, and 9!*8 and 9!*9 give us only a 7-digit numbers
        s = 0
        for d in range(len(str(n))):
            s+=factorials[int(str(n)[d])]
        if s==n:
            print n
            total+=n
    return total
