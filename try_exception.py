number = input("type a number:")

try:
    number = float(number)
    print("the number is: ", number)
except:
    print("Invalid Number")
