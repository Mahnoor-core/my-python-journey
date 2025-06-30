a = "Simple Calculator"
print(a.center(40, "-"))
print("\n")

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
op = input("Enter operation: ")

match op:
    case "+":
        print("Answer: ", num1 + num2)
    case "-":
        print("Answer: ", num1 - num2)
    case "*":
        print("Answer: ", num1 * num2)
    case "/":
        print("Answer: ", num1 / num2)
    case "%":
        print("Answer: ", num1 % num2)
    case "//":
        print("Answer: ", num1 // num2)
    case "**":
        print("Answer: ", num1 ** num2)
    case _:
        print("Invalid operation")


