def char_frequency(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

input_string = "hello world, this is a test string."
char_freq = char_frequency(input_string)
print("Character Frequencies:")
for char, freq in char_freq.items():
    print(f"{char}: {freq}")