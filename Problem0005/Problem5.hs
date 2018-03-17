-- What is the smallest positive number that is evenly divisible 
-- by all of the numbers from 1 to 20?

-- We can start out with some of the work we did back in Problem 3.
isPrime :: Int -> Bool
isPrime n = divisibleBy 2
    where
        divisibleBy d  -- recursive helper function
            | d*d > n           = True
            | n `rem` d == 0    = False
            | otherwise         = divisibleBy (d+1)

primes :: [Int]
primes = filter isPrime (2:[3, 5..])
-- We know we'll need at least all of the primes less than 20.
-- just using the primes though, we get 
-- product (takeWhile (<= 20) primes)
-- 9699690
-- which simple testing will show is not divisible by 4.
-- why?
-- It's pretty plain that the factors of 9699690 are 
-- [2,3,5,7,11,13,17,19]
-- and the factors of 4 are
-- [2, 2]
-- Right there we see our problem, 
-- we are missing the second 2 that would make our number 
-- divisible by 4.
-- So our real challenge here is how to we include the 
-- additional copies of the primes we need?

-- A bit more investigating of the numbers less than 20
-- that do not evenly divide 9699690
-- we start to see the pattern that they each involve 
-- a power of a prime.
-- So we just need to append all the powers of primes
-- less than 20 to our list of primes less than 20.
primePowers :: Int -> [Int]
primePowers n = powers primes 1
    where
        powers xs@(x:y) e
            | x^e <= n      = x:(powers xs (e+1))
            | x > n         = []
            | otherwise     = powers y 1

-- product (primePowers 20)
-- 232792560