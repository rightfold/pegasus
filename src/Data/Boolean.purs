module Data.Boolean where

foreign import conj :: Boolean -> Boolean -> Boolean

disj :: Boolean -> Boolean -> Boolean
disj false x = x
disj x false = x
disj true true = true
