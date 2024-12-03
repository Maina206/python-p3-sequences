#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    elif length == 2:
        print([0, 1])
        return

    fibonacci_sequence = [0, 1]

    for i in range(2, length):
        next_fib = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_fib)

    print(fibonacci_sequence)
    pass

# Example usage:
print_fibonacci(10)
