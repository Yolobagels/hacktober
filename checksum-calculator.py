# This program calcualtes the checksum of popular Singapore IDs

option = input("Enter the corresponding number for the checksum you would like to validate \n1. NRIC \n2. Carplate \n3. UEN\n")
if option == "1":
    nric = input("Enter your NRIC: ")
    nric = nric.upper()
    if len(nric) != 9:
        print("Invalid NRIC")

elif option == "2":
    carplate = input("Enter your carplate: ")
    carplate = carplate.upper()
    if len(carplate) != 7:
        print("Invalid carplate")

elif option == "3":
    uen = input("Enter your UEN: ")
    uen = uen.upper()
    if len(uen) != 9:
        print("Invalid UEN")