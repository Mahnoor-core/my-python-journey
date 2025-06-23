# In python, we directly take user input by using input()

a = input()
print(a)

# We can also add a statement to the input statement, just like this

b = input("Enter your name: ")
print(b)

# But by default input statement take the input as string, for example

c = input("Enter first number: ")
d = input("Enter second number: ")
print(c + d)

# To convert into other data type, we use typecasting

e = int(input("Enter first number: "))
f = int(input("Enter second number: "))
print(e + f)
