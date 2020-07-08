import random

print("program for user enter names and print random name")

people = []

for x in range(0,8):
    person = input("Please enter a name: ")
    people.append(person)

index = random.randint(0,7)

random_person = people[index]

print("Picked random person is:" , random_person)