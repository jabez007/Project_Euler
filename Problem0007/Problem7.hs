-- What is the 10,001st prime number?

-- Again, our work in Problem 3 can help us greatly
isPrime :: Int -> Bool
isPrime n = divisibleBy 2
    where
        divisibleBy d  -- recursive helper function
            | d*d > n           = True
            | n `rem` d == 0    = False
            | otherwise         = divisibleBy (d+1)

primes :: [Int]
primes = filter isPrime (2:[3, 5..])
-- So much so that with Haskell's lazy lists
-- this solution is as easy as
-- primes !! 100000
-- (10000 instead of 10001 since the list index starts at 0)
-- which returns in under a minute with
-- 104743