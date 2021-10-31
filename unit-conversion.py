# This program converts an input number from pounds to kilograms

lbs_to_kg = 0.453592

# User input
num = eval(input('Enter a number you wish to convert from pounds to kg: '))

# Evaluate mass in kg
num_kg = num * lbs_to_kg

# Print result
print('{0} lbs is {1:0.3f} kg'.format(num, num_kg))
