# A match statement will compare a variables value to diff patterns 
# Once a pattern is matched it execute the code of that pattern

x = int(input("Enter a number: "))

match x:
    case 0:
        print("Equals to zero")
    case 1:
        print("Equals to one")
    case 2:
        print("Equals to two")
    case _:
        print("Another number")     # For default statement we use ' _ '



# We can also use if statement in cases

match x:
    case _ if x>0:
        print(x, "is positive")
    case _ if x<0:
        print(x, "is negative")
    case _:
        print(x, "is zero")