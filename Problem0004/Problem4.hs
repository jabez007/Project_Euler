-- Find the largest palindrome made from the product of two 3-digit numbers.

-- Figuring out if something is a palindrome is pretty straight forward.
-- For strings and such, we can just use reverse
isPalindrome x = x == reverse x
-- But we can't exactly do this with integers.
-- What we can do is change the integer into a string.
isPalindrome' :: Int -> Bool
isPalindrome' x = y == reverse y
    where y = show x

-- So if we have a list of candidates palindromes, 
-- we can essentially apply a filter to is to find the actual palindromes.
findPalindromes [] = []
findPalindromes xs@(x:y)
    | isPalindrome x  = x:(findPalindromes y)
    | otherwise       = findPalindromes y

findPalindromes' :: [Int] -> [Int]
findPalindromes' [] = []
findPalindromes' xs@(x:y)
    | isPalindrome' x  = x:(findPalindromes' y)
    | otherwise        = findPalindromes' y

-- Now all we need is to come up with our list of candidate palindromes.
-- Instead of just using [x*y | x <- [100..999], y <- [100.999]]
-- and doing lots of duplicative multiplication work,
-- we can narrow our search to the product of each 
-- of the 2-combinations of [100..999].
combinations :: Int -> [a] -> [[a]]
-- We don't actually need this base case; it's just here to
-- avoid the warning about non-exhaustive pattern matches
combinations _ [] = [[]]
-- Base case--choosing 0 elements from any list gives an empty list
combinations 0 _  = [[]]
-- Get all combinations that start with x, recursively choosing (k-1) from the
-- remaining xs. After exhausting all the possibilities starting with x, if there
-- are at least k elements in the remaining xs, recursively get combinations of k
-- from the remaining xs.
combinations k (x:xs) = x_start ++ others
    where 
        x_start = [ x : rest | rest <- combinations (k-1) xs ]
        others  = if k <= length xs then combinations k xs else []

-- maximum (findPalindromes' [product x | x <- combinations 2 [999,998..100]])
-- Its slow because we are still doing more multiplications than we need to.
-- It does come back in less than a minute though.
-- 906609
