# Default arguments

def average(a=9, b=1):      # a and b have default values
    print("Average =", (a + b)/2)
average()
average(5,15)               # In this case override values are calculated
print("--------")


# Required arguments

def average(a, b=4):        # Here a is required argument
    print("Average =", (a + b) / 2)
average(4)                  # We must have to assign it a value
print("--------")

