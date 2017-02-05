module Data.Tuple where

import Data.Eq (class Eq, eq)

data Tuple a b = Tuple a b

instance eqTuple :: (Eq a, Eq b) => Eq (Tuple a b) where
  eq (Tuple a b) (Tuple c d) = if eq a c then eq b d else false

fst :: ∀ a b. Tuple a b -> a
fst (Tuple x _) = x

snd :: ∀ a b. Tuple a b -> b
snd (Tuple _ x) = x
