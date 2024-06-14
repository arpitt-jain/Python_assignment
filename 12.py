def sum_of_digits(number):
    number_str = str(number)
    total_sum = 0
    
    for digit in number_str:
        total_sum += int(digit)
    
    return total_sum

number = int(input("Enter a number: "))

sum_digits = sum_of_digits(number)

print(f"The sum of the digits of the number {number} is: {sum_digits}")
