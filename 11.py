def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence[:n]  
n = int(input("Enter the number of Fibonacci numbers to generate: "))
fib_sequence = fibonacci_sequence(n)
print(f"The first {n} numbers in the Fibonacci sequence are: {fib_sequence}")
