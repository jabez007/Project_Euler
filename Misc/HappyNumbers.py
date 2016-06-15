#Finding if a number is happy

def happy(x):
        z=x
        while x!=1 and x!=2 and x!=4:
                y=0
                for i in range(10, -1, -1):
                        y+=(x/(10**i))**2
                        x=x%(10**i)
                x=y
                print x
        if x==1:
                print "\n",z,"is happy!"
        else:
                print "\n",z,"is not happy...."
        main()

def main():
        number=input("Enter the number that you wish to find out if its happy: ")
        if number>0:
                happy(number)

main()

'''Alternate
for i in range(len(str(number))):
	digitSum = digitSum+int(str(number)[i])**2
''''
