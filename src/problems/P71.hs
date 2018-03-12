{- Problem 71: Ordering reduced fractions.
 -
 - A reduced proper fraction is defined as n/d for integers n, d where n < d
 - and HCF(n, d) = 1.
 -
 - The problem is to find in the ordered list of all reduced proper fractions
 - with d <= 1,000,000, the numerator of the fraction immediately preceding
 - 3/7. -}

module Main where

    targetNum = 3
    targetDenom = 7
    target = (fromIntegral targetNum) / (fromIntegral targetDenom)
    dLimit = 1000000

    -- Find the highest common factor of two integers, using Euclid's
    -- algorithm.
    hcf :: Integer -> Integer -> Integer
    hcf a 0 = a
    hcf a b = hcf b $ a `mod` b

    -- For a given denominator d, find the largest value of n that gives a
    -- valid reduced proper fraction. A fraction n/d is reduced proper iff
    -- n < d and HCF(n, d) = 1.
    findN :: Integer -> Maybe Integer
    findN d = findNRecur d (startN d)
        where
        startN :: Integer -> Integer
        startN d =
            let targetN = floor $ (fromIntegral d) * target in
            if d `mod` targetDenom == 0 then targetN - 1 else targetN

        findNRecur :: Integer -> Integer -> Maybe Integer
        findNRecur d n
            | n < 1 = Nothing
            | hcf n d == 1 = Just n
            | otherwise = findNRecur d $ n - 1

    -- Generate a list of the largest fractions < 3 / 7 for each value of d,
    -- filtering out any with no valid fractions.
    fracs :: [(Integer, Integer)]
    fracs = [(n, d) | (Just n, d) <- baseFracs]
        where
        baseFracs :: [(Maybe Integer, Integer)]
        baseFracs = [((findN d), d) | d <- [1..dLimit]]

    -- From the list of reduced proper fractions, find the numerator of the largest
    -- fraction. This will be the one immediately preceding 3/7.
    findFracN :: (Fractional a, Ord a) => [(Integer, Integer)] -> a -> Integer -> Integer
    findFracN [] maxFrac maxFracN = maxFracN
    findFracN ((n, d):restFrac) maxFrac maxFracN =
        let frac = (fromIntegral n) / (fromIntegral d) in
        if frac > maxFrac then findFracN restFrac frac n
        else findFracN restFrac maxFrac maxFracN

    resultN = findFracN fracs 0 0

    main :: IO ()
    main = print resultN

