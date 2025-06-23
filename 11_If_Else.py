# Sometimes we need conditions to execute a program
# In python, these are
#       if statement
#       if else statement
#       elif statement
#       nested if else statement

# For example -> if
age = int(input("Enter your age: "))
print("Your age is", age, "\n")
if(age>=18):
    print("You can drive\n")


# For example -> if else
age = int(input("Enter your age: "))
print("Your age is", age)
if(age>=18):
    print("You can drive\n")
else:
    print("You can't\n")


# For example -> elif
num = int(input("Enter a number: "))
if(num>0):
    print("Positive number\n")
elif(num<0):
    print("Negative number\n")
else:
    print("Zero\n")


# For example -> nested if else
age = int(input("Enter your age: "))
print("Your age is", age)
if (age >= 18):
    ans = input("Do you have license?")
    if(ans=="yes"):
        print("You can drive\n")
    else:
        print("You can't\n")
else:
    print("You can't\n")
