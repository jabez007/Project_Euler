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
-- which returns in under a minute

-- It's so slow because we are using divisions
-- and we are dividing by more numbers than needed.
-- We only need to test division with the known primes 
-- up to the square root.
-- A simple improvment then would be
primes' :: [Int]
primes' = 2 : filter (isPrime' primes') [3,5..]
  where 
    isPrime' (p:ps) n
        | p*p > n           = True
        | n `rem` p == 0    = False
        | otherwise         = isPrime' ps n
-- which returns in about half the time as before.
-- But is still incredibly slow when trying to find 
-- primes just one more order of magnitude further
-- in the list.

-- The problem is that we are still using trial division.
-- We can get away from this method by looking at the 
-- sieve of Eratosthenes
primes'' = 2 : g (fix g)
    where
        g ps = 3 : (gaps 5 (unionAll [[p*p, p*p+2*p..] | p <- ps]))

fix g = zs 
    where 
        zs = g zs

gaps k s@(x:xs) 
    | k < x         = k:gaps (k+2) s    
    | otherwise     = gaps (k+2) xs 

unionAll ((x:xs):t) = x : union xs (unionAll (pairs t))
    where
        pairs ((x:xs):ys:t) = (x : union xs ys) : pairs t

union (x:xs) (y:ys) = 
    case compare x y of 
        LT -> x : union xs (y:ys)
        EQ -> x : union xs ys 
        GT -> y : union (x:xs) ys
union xs [] = xs
union [] ys = ys
-- This comes back in about half the time as our
-- improved trial division for the 10,001st prime,
-- and comes back in under a minute for the 
-- 100,001st prime.

-- 104743
