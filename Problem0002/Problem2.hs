-- By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
-- find the sum of the even-valued terms.

-- Implementing the Fibonacci sequence is considered the "Hello, world!" of Haskell programming.
-- The definition of the Fibonacci sequence can be written in Haskell simply as a recursive function.
fib :: Int -> Int
fib 0 = 0
fib 1 = 1
fib n = fib (n-1) + fib (n-2)
-- The downside to this recursive implementation is that it requires O(fib n) additions.
-- That is, to calculate the 9th Fibonacci number requires 34 additions.

-- Haskell's lazy lists and list comprehension allows us to shortcut this.
-- We can generate an 'infinite' list of the Fibonacci sequence with a strange looking recursive function.
fibs :: [Int]
fibs = 1 : 1 : zipWith (+) fibs (tail fibs)
-- To visualize how this function works,
-- Assume you already had an infinite list of the Fibonacci numbers:
-- [ 1, 1, 2, 3, 5, 8, 13, .... ]
-- The tail of our list is:
-- [ 1, 2, 3, 5, 8, 13, 21, .... ]
-- Then zipWith works like zip, 
-- only instead of combining two lists element by element into pairs 
-- it combines our two lists element by element using the given operator (+):
--    [ 1, 1, 2, 3,  5,  8, 13, .... ]
-- +  [ 1, 2, 3, 5,  8, 13, 21, .... ]
-- =  [ 2, 3, 5, 8, 13, 21, 34, .... ]
-- Suddenly, we have the Fibonacci sequence just missing the first two elements.
-- Our function accounts for that (and gets the recursion started) 
-- by appending the elements 1 and 1 to the front.

-- Then we just grab the nth element of that list
fib' :: Int -> Int
fib' n = fibs !! n
-- Using this, fib' 100 comes back almost immediately while fib 100 takes several minutes.

-- Returns the sum of the numbers from the Fibonacci sequence 
-- that are evenly divisible by m 
-- and less than or equal to n
sumFibs :: Int -> Int -> Int
sumFibs m n = sum [x | x <- (takeWhile (<= n) fibs), x `mod` m == 0]  -- use takeWhile for infinite lists 

-- Now we just need to sum the even numbers less than 4,000,000 from the Fibonacci sequence
-- sumFibs 2 4000000
-- and the answer comes back almost immediately
-- 4613732
