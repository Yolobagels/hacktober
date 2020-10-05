# This program finds the square root of a number. It can be real or complex.
# Import complex math module
import cmath

# User input
num = eval(input('Enter a number: '))

# Evaluate square root
num_sqrt = cmath.sqrt(num)

# Print result
print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num, num_sqrt.real, num_sqrt.imag))
