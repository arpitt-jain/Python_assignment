def find_min_max(numbers):
    if not numbers:
        return None, None  

    min_value = max_value = numbers[0]

    for num in numbers:
        if num < min_value:
            min_value = num
        elif num > max_value:
            max_value = num

    return min_value, max_value

numbers = [3, 1, 4, 10, 2, 6]
min_val, max_val = find_min_max(numbers)
print(f"Minimum value: {min_val}")
print(f"Maximum value: {max_val}")