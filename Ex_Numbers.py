import math

print("Program to calculate the area and circumference of circle")

radius = float( input("Please enter radius of circle: "))

area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius


print("Circle Area is ", round (area, 2))
print("Circle circumference is ", round (circumference,2))
