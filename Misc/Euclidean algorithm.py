#Euclidean Algorithm for finding the greatest common divisor of two numbers.
def main():
    number1=input("You are looking for the Greatest Common Divisor of? ",)
    number2=input("and? ")
    if number1>0 or number2>0:
        EA(number1, number2)

def EA(x, y):
    if x%y==0:
        print x,"is a multiple of",y
        main()
    elif y%x==0:
        print y,"is a multiple of",x
        main()
    elif x>y:
        while x%y!=0:
            a=x%y
            x=y
            y=a
        print "The Greatest Common Divisor is",a
        main()
    elif y>x:
        while y%x!=0:
            a=y%x
            y=x
            x=a
        print "The Greatest Common Divisor is",a
        main()

main()
