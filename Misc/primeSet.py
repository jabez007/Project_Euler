def primeSet(x):
	prime=[2]
	for i in range(x):
		m=1
		for j in range(len(prime)):
			if j<len(prime):
				m=m*prime[j]
		prime=prime+[m+1]
	print prime
	main()

def main():
    setOfPrimes=input("How big do you want the set? ")
    if setOfPrimes>=1:
        primeSet(setOfPrimes)
        
main()
