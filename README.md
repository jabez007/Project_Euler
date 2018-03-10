# Project Euler (Python)

## Synopsis

These are my solutions for the problems of Project Euler done in 
Python 2.7 using only the basic libraries and builtin functions that 
come with Python


## Motivation

I'm combining my love of mathematics with my desire to improve my 
programming skills and knowledge of Python.


## References

Several of the function and class that I've created in these solutions
are reused in other solutions and can be reused outside of Project 
Euler. I've to include those here
+ From Problem3
  + prime_factorization(n) - inefficient "trial and error" method to 
    find the prime factors and their exponents of n
  + eratosthenes_sieve(n=100) - finds all of the prime numbers up to n 
    using the Sieve of Eratosthenes
+ From Problem7
  + is_prime(n) - (very inefficient) determine if a given number is 
    prime by attempting to divide it by each of the primes up to the 
    square root of the number. If we haven't found a factor by then, 
    we won't.
+ From Problem8
  + product(factors) - Calculates the product of the given factors, 
    similar to the Python builtin sum function
+ From Problem15
  + multiply_matrices(a, b) - multiplies two matrices together. 
    Does NOT validate that the two matrices can be multiplied together, 
    that is it does not compare the dimensions of the matrices to 
    determine their compatibility
  + matrix_power(matrix, exponent) - raises the given matrix to the 
    given power through matrix multiplication
+ From Problem20
  + factorial(n) - recursively calculates the factorial of n.
+ From Problem21
  + get_proper_divisors(n) - Finds all of the proper divisors of n


## License

A short snippet describing the license (MIT, Apache, etc.)
