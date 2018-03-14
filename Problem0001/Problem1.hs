-- Find the sum of all the multiples of 3 or 5 below 1000.

-- Multiples of m less than n
-- returns the list of natural numbers below n that are multiples of m
multiples :: Int -> Int -> [Int]
multiples m n = [m*x | x <- (takeWhile (< (n `div` m) + 1) [1..]), m*x < n]  -- `div` gives us the integer quotient instead of a float.

-- let threes = sum multiples 3 1000
-- let fives = sum multiples 5 1000
-- let initialSum = sum [threes, fives]
-- we can see that we will inevitably have an overlap with the threes list and the fives list, 
-- so we end up summing some numbers twice.
-- we can account for those by finding the multiples of the least common multiple (lcm) between 3 and 5,
-- and subtracting their sum from our over-counted sum.

-- it is easy to see here that the lcm is 15,
-- but for more difficult problems we can calculate the lcm of a and b by |a*b|/gcd(a, b)
-- where gcd is the greatest common denominator that we would also need to calculate.
-- luckily, Haskell has both gcd and lcm as builtin functions.
-- let fifteens = sum multiples 15 1000
-- sum [initialSum, -fifteens]

-- Sum of all multiples of a or b below n
sumMultiples :: Int -> Int -> Int -> Int
sumMultiples a b n = sum [multiplesA, multiplesB, -multiplesLCM]
    where multiplesA = sum (multiples a n); multiplesB = sum (multiples b n); multiplesLCM = sum (multiples (lcm a b) n)

-- sumMultiples 3 5 1000
-- 233168
