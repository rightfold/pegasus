module Data.Array where

empty :: ∀ a. Array a
empty = []

singleton :: ∀ a. a -> Array a
singleton x = [x]

isEmpty :: ∀ a. Array a -> Boolean
isEmpty [] = true
isEmpty _  = false
