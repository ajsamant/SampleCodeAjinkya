print("Program for user details")

f_name = input("Please enter your first name: ")
m_name = input("Please enter your middle name: ")
l_name = input("Please enter your last name: ")

print("Your initials are ", f_name[0], m_name[0], l_name[0]) 


print("__________________________________________________________________________") 

print("Program for product details")

lot_number = "037-00901-00027"
print("My product code is ", lot_number)
print("Lot number in details")
print("Country code: ", lot_number[:3], "Product code: ", lot_number[4:9], "Batch Number: ", lot_number[10:] )