# Strings are immutable, these cannot be changed once created
# But we can make a copy of them

a = "Hello"
print(a.upper())  # Its a new string with all upercase letters
                  # But the previous string doesn't change

print(a)          # This will type Hello

# Similarly there is also lower case function
print(a.lower())


'''>>---------<<'''

# Here are some methods for strings


# rstrip() removes any trailing character from string
b = "!!Maha!!!"
print(b.rstrip("!"))        # It doesn't remove leading characters


# replace() replaces a string with other string
print(b.replace("Maha","Mahnoor"))


# capitalize() capital the first letter of the string
    # but lower all the other characters
c = "my namE is Mahnoor"
print(c.capitalize())


# center() aligns the string to center according to the parameter given by the user
d = "Welcome to my coding journey"
print(d.center(50))
# Also we can use 
print(d.center(50,"."))


# count() counts that how many times a character is used in the string
print(a.count("l"))
print(d.count("Welcome"))


# endswith() tells us about the existance of any string that ends with given parameter
print(b.endswith("!"))      # returns boolean expression


# find() searches the first occurence of the given value in the string and returns the index
print(d.find("to"))
# If there is no such occurence it will return -1
print(d.find("is"))

# There are many more methods that we use in our upcoming codes