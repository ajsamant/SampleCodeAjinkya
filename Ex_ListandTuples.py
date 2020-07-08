print("Printing list of people and adding new name and display updated script")

people_names = ["Anthony", "Tanvee", "Rashmi", "Anurag", "Akshatha"]

new_user = input("Please enter your name: ")

people_names.append(new_user)

print(people_names)

print("__________________________________________________________________________") 
print("__________________________________________________________________________") 
print("__________________________________________________________________________") 


print( "Program for displaying month in a birthday using TUPLES")

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
birth_date = input("Please enter your birthday [Format : DD-MM-YYYY]: ")

index = int(birth_date[3:5]) - 1
month_born = months[index]
#month_born = months [int(birth_date[3:5] - 1)]

print("You were born in ", month_born)