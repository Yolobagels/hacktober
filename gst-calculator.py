#This program calculates the amount of GST payable

option = input("Is there GST? (Y/N)")
gross = float(input("Enter the gross amount: "))
gst = 0
if option == "Y" or option == "y":
    gst = gross * 0.07
    print("The GST payable is: ", gst)
else:
    print("No GST payable")
print("The final amount payable is", gross + gst)