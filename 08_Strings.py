# A string is basically a sequence of textual data

name = "Mahnoor"
name = 'Maha'       # Note: Strings can be inclosed in single or double quotes
print(name)

# To write multipe line string, we can use triple quotes

greetings = """Hi Maha, 
Welcome...
How are you?"""
print(greetings)

# In python, strings is like an array of characters
# We can access parts of strings by using index 

print(name[0])
print(name[1])
print(name[2])
print(name[3])
# print(name[4])    Throws an error

# We can also access all these characters using loops

print("Accessing characters using loop")
for character in name:
    print(character)        # We should learn about this in coming topics