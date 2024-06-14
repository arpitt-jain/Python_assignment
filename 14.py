lines = []

print("Enter multiple lines of text. Press Enter on an empty line to stop.")

while True:
    line = input()
    if line == "":
        break  
    lines.append(line)  
print("\nThe entered lines are:")
for line in lines:
    print(line)
