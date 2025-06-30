# The break statement enables to terminate a loop

for i in range(20):
    print("5 x", i, "=", 5*i)
    if i==10:
        break       # When i becomes 10 the loop ends
print("---------")

# Continue statement skips the rest of the loop and execute next iteration

for i in range(11):
    if i == 5:
        print("Skips the iteration")
        continue
    print("5 x", i, "=", 5 * i)
