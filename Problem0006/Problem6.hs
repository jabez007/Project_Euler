-- Find the difference 
-- between the sum of the squares of the first one hundred natural numbers 
-- and the square of the sum.

-- Solving this in Haskell is almost trivial
sumPower n e = sum [x^e | x <- [1..n]]
powerSum n e = (sum [1..n])^e

-- (powerSum 100 2) - (sumPower 100 2)
-- 25164150