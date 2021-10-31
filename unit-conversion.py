# This program converts an input number from pounds to kilograms

lbs_to_kg = 0.453592

# User input
option = eval(input("Enter 1 to convert from pounds to kilograms, or 2 to convert from kilograms to pounds: "))
if option == 1: 
    pounds = eval(input("Enter a number of pounds: "))
    kilograms = pounds * lbs_to_kg
    print("The number of kilograms is", kilograms)
elif option == 2:
    kilograms = eval(input("Enter a number of kilograms: "))
    pounds = kilograms / lbs_to_kg
    print("The number of pounds is", pounds)
