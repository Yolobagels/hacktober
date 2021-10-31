# This program converts temperature from Celsius to Fahrenheit and vice versa.

option = input("Enter 'C' to convert from Celsius to Fahrenheit or 'F' to convert from Fahrenheit to Celsius: ")
if option == 'C':
    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius * 9/5 + 32
    print("The temperature in Fahrenheit is", fahrenheit)
elif option == 'F':
    fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("The temperature in Celsius is", celsius)
else:
    print("You did not enter 'C' or 'F'")