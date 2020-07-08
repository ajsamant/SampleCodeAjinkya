blog_posts = [" ","a","b","c"," ","d","e"]

for post in blog_posts:
    if post == " ":
        continue
    else:
        print(post)

print("-----------------------")

myString = "This is a string"

for char in myString:
    print(char)

print("-----------------------")

for x in range(0,10):
    print(x)

print("-----------------------")

person = {"Name":"Ajinkya","Age":28,"Gender":"Male"}

for key in person:
    print(key, ":" , person[key])

          
print("-----------------------")

blog_posts = {"Python": ["a","b","c","d","e"], "JavaScript": ["f"]}

for cat in blog_posts:
    print("Post about", cat)
    for post in blog_posts[cat]:
        print(post)
