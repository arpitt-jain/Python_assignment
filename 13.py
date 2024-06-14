birthyear = int(input("Enter your birth year: "))

import datetime
currentyear = datetime.datetime.now().year

age = currentyear - birthyear

print(f"You are {age} years old.")
