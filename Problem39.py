#Project Euler, problem 39
#For which perimeter of a right triangle are the number of pythagorean triples maximized

sols = [0]*1001

for a in range(1,1001):
    for b in range(1,1001):
        c = ((a**2)+(b**2))**.5
        if c==int(c): #check that we have a pythagorean triple
            p = int(a+b+c)
            if p>1000:
                break
            else:
                sols[p]+=1

print sols.index(max(sols))
    
