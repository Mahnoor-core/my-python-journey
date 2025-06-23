import time

current_time = time.strftime("%H:%M:%S")
print("It's", current_time)

if ("06:00:00" <= current_time < "12:00:00"):
    print("Good Morning Sir! ☺️")

elif("12:00:00" <= current_time < "17:00:00"):
    print("Good Afternoon Sir! 🫡")

elif("17:00:00" <= current_time < "21:00:00"):
    print("Good Evening Sir! 🙂")

else:
    print("Good Night Sir!...🥱") 
