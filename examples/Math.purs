module Math where

import Data.Tuple (Tuple(..))
import Prelude

divmod :: ∀ a. (EuclideanRing a) => a -> a -> Tuple a a
divmod a b = Tuple (a `div` b) (a `mod` b)
