#Inverse Factorial - ?

def inverseFactorial(n):
    a=n
    x=2.0
    y=0
    while (a/x)!=1 and (a-int(a))==0:
        a/=x
        if (a-int(a))!=0:
            print n,"does not have an inverse factorial."
            y=1
        x+=1
    if y!=1:
        print n,"is the factorial of",int(x)
    main()

def main():
    number=input("What number do you want to find the inverse factorial of? ")
    if number>0:
        inverseFactorial(number)

main()
