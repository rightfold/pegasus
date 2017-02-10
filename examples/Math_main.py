import Data_EuclideanRing
import Math

print('Expecting 8 and 2.')
pair = Math.divmod(Data_EuclideanRing.euclideanRingInt)(42)(5)
print(pair.value0, pair.value1)
