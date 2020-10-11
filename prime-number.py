# This program checks if an input number is prime or not

# User input
num = eval(input('Enter a number that you would like to check if its prime: '))

# Evaluate if the number is prime
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            print(i, "x", num//i, "=", num)
            break

    else:
        print(num, "is a prime number")
    
else:
    print(num, "is not a prime number")
