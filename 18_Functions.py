# A function is a block of code that performs a specific task whenever it is called


# ADD Function
def add(a,b):
    sum = a + b
    print(sum)      # This is a block of function which executes every time we call it

c = 7
d = 4
add(c, d)

e = 5
f = 95
add(e, f)           # We do not need to repeat  sum = a + b
#                           print(sum)


def subtract(a, b):
    pass            # pass says that the function body is written later


# We can also use return statement
# LIKE this
def add(a, b):
    return a + b
c = add(3, 6)
print(c)