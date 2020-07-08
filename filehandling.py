f = open("text.txt", "a")
print(f.write("\nThis text willl overwrite the content of the file"))

f = open("text.txt", "r")
print(f.read())
