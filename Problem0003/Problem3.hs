-- What is the largest prime factor of the number 600851475143?

-- First, simply finding if a number is prime or not can be done 
-- through a trial division that stops at the square root.
isPrime :: Int -> Bool
isPrime n = divisibleBy 2
    where
        divisibleBy d  -- recursive helper function
            | d*d > n           = True
            | n `rem` d == 0    = False
            | otherwise         = divisibleBy (d+1)

-- Using this trial division to get a list of primes
-- is easy, especially by skipping even numbers (except 2) 
-- as candidate divisors which halves the number of required divisions.
primes :: [Int]
primes = filter isPrime (2:[3, 5..])

-- Then using this list of primes, 
-- we can divide out the factors of our number
factorize :: Int -> [Int]
factorize n
    | isPrime n    = [n]
    | otherwise    = factor n primes  -- this is an infinite list, but the magic of Haskell's lazy lists saves us.
    where
        factor d (x:xs)
            | d `rem` x == 0    = [x]++(factorize (d `div` x)) 
            | otherwise         = factor d xs

-- This looks messy, and can probably be done more efficiently
-- but our solution for this particular problem returns
-- almost immediately as is.
-- factorize 600851475143
-- [71,839,1471,6857]