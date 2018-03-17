-- Find the difference 
-- between the sum of the squares of the first one hundred natural numbers 
-- and the square of the sum.

-- Solving this in Haskell is almost trivial
sumPower n e = sum [x^e | x <- [1..n]]
powerSum n e = (sum [1..n])^e
-- This returns in under a minute all the way up to
-- 10000000

-- But we are still doing a lot of work we don't need to.
-- First, sum [1..n] is a simple geometric series 
-- which has a well known formula.
-- This allows us to greatly improve our powerSum
powerSum' n e = ((n*(n+1))/2)^e
-- Second, sum [x^e | x <- [1..n]] is a simple power series.
-- Unfortunately this power series does not have a formula
-- for the generic case, so we'll have to focus on the 
-- specific case of sum [x^2 | x <- [1..n]]
sumSquares n = ((n^3)/3) + ((n^2)/2) + (n/6)

-- (powerSum' 100 2) - (sumSquares 100)
-- 25164150