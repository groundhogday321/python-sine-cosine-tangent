



import math
import numpy
from fractions import Fraction

# *** SINE ***
print('\nTrigonometric SINE')

# sine input as radians
sine_radians = math.sin(0.523599)

# display sine normal and rounded (radians)
print('sine of 0.523599 radians (30 degrees) is', sine_radians, 'rounded', round(sine_radians, 2))
# prints sine of 0.523599 radians (30 degrees) is 0.5000001943375613 rounded 0.5

# sine input as degrees
sine_degrees = math.sin(math.radians(30))

# display sine normal and rounded (degrees)
print('sine of 30 degrees is', sine_degrees, 'rounded', round(sine_degrees, 2))
# prints sine of 30 degrees is 0.49999999999999994 rounded 0.5

# display sine as fraction ratio
print('sine of 30 degrees ratio is', Fraction(sine_degrees).limit_denominator())
# prints sine of 30 degrees ratio is 1/2

# example using numpy
sine_with_numpy = numpy.sin(numpy.deg2rad(30))
print('sine of 30 degrees using numpy is', Fraction(sine_with_numpy).limit_denominator())
# prints sine of 30 degrees using numpy is 1/2

# *** COSINE ***
print('\nTrigonometric COSINE')

# cosine
cosine_degrees = math.cos(math.radians(60))
print('cosine of 60 degrees is', round(cosine_degrees, 2), 'or', Fraction(cosine_degrees).limit_denominator())
# prints cosine of 60 degrees is 0.5 or 1/2

# *** TANGENT ***
print('\nTrigonometric TANGENT')

# tangent
tangent_degrees = math.tan(math.radians(45))
print('tangent of 45 degrees is', round(tangent_degrees, 2))
# prints tangent of 45 degrees is 1.0
