# To find length of strings, we use len()

a = "Hey"
print(len(a))

# Similarly

fruit = "Mango"
length = len(fruit)
print("Mango has ", length, "letters")

'''--------------'''


# If we want to access some letters from a string, we use :

print(fruit[0:3])       # It will give us Man
print(fruit[1:4])       # If we want to access from mid
print(fruit[:3])        # It will automatically access from 0
print(fruit[:])         # It will access from 0 to 5 automatically
