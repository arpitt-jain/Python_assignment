filename = "output.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
    print("File content:")
    print(content)

except FileNotFoundError:
    print(f"The file {filename} does not exist.")
