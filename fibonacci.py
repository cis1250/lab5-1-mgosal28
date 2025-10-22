#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)
def get_input(): #gets number from user and checks if it is valid
    while True:
        user_input = input("How many Fibonacci terms do you want? ")
        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)
        else:
            print("Please enter a positive number.")

def generate_fibonacci(n):
    fib = []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a) #adds value a to the fib list
        a, b = b, a + b
    return fib

def print_fibonacci(fib_sequence):
    print("Fibonacci sequence:")
    for num in fib_sequence:
        print(num, end=" ")
    print()

# Main part of the program
terms = get_input()
sequence = generate_fibonacci(terms)
print_fibonacci(sequence)
