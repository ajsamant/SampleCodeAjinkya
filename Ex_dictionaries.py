print("dic for person and user will ask about information")

person = {"name":"Ajinkya","gender":"Male","address":"Toronto","phone": 5488881681 }

key = input("Please enter what information would like to know about: ").lower()

result = person.get(key,"Invalid Input")

print(result)