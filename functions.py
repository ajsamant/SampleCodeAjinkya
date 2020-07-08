def say_hello(person1, person2="Akshatha"):
    print("Hello! " + person1 + ", how are you doing? " + person2 + " is waiting for you.")

say_hello("Ajinkya", "Anurag")

def far2cel(far):
    cel = (5 * (far - 32)) / 9
    return cel

print("Celsius: " , round (far2cel(100), 2))
print("Kelvin: " , round (far2cel(100) + 273.5, 2))