# The conversion of one data type into another is called type casting

a = "2"
b = "4"
print(a + b)       # It concatenate the both bcz both are considered strings

# But if we want to add both we typecast it

print(int(a) + int(b))       


# There are two types of typecasting 

# ---> Explicit type casting
        # The type casting done by programmer itself 
        # like the above example

# ---> Implicit type casting
        # The type casting done by python interpreter automatically
       
c = 1.9 
d = 8
print(c + d)        # Here the value of d is auotmatically converted into float and then added

