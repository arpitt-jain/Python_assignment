import re

def remove_punctuation(s):
    return re.sub(r'[^\w\s]', '', s)

input_string = "Hello, World! This is a test string."
output_string = remove_punctuation(input_string)
print(f"Original string: {input_string}")
print(f"String without punctuation: {output_string}")