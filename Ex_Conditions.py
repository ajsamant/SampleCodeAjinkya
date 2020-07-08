print("Program to calculate BMI of a person and result to display overweight or Normal")

u_height = float (input("Please enter your height in meter: "))
u_weight = float(input("Please enter your weight in kg. :"))

bmi = u_weight / (u_height * u_height)

print("Your BMI is ", round(bmi,2))

if(bmi <= 18.5):
    print("User BMI is underweight")
elif(bmi > 18.5 or bmi<=24.9):
    print("User BMI is Normal Weight")
elif(bmi > 24.9 or bmi <=29.9):
    print("User BMI is Overweight")
else:
    print("User BMI is Obesity")