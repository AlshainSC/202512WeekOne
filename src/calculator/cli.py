#!/usr/bin/env python3
"""
Command-line interface for the calculator application.
"""

from operations import add, subtract, multiply, divide, SUPPORTED_OPERATIONS


def display_welcome():
    """Display the welcome message."""
    print("=================================")
    print("  Welcome to Python Calculator!")
    print("=================================")
    print(f"Available operations: {', '.join(SUPPORTED_OPERATIONS)}")
    print("Type 'quit' to exit.")
    print()


def get_number(prompt):
    """Get a number from the user. Returns None if user wants to quit."""
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'quit':
            return None
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a number or 'quit'.")


def get_operation():
    """Get a valid operation from the user."""
    while True:
        operation = input("Enter operation: ").lower()
        if operation == 'quit':
            return None
        if operation in SUPPORTED_OPERATIONS:
            return operation
        print(f"Invalid operation. Choose from: {', '.join(SUPPORTED_OPERATIONS)}")


def calculate(a, operation, b):
    """Perform the calculation and return the result."""
    operations = {
        'add': (add, '+'),
        'subtract': (subtract, '-'),
        'multiply': (multiply, '*'),
        'divide': (divide, '/')
    }
    
    func, symbol = operations[operation]
    result = func(a, b)
    
    if result is None:
        return f"Error: Cannot divide by zero"
    
    # Format numbers nicely (remove .0 for whole numbers)
    a_str = int(a) if a == int(a) else a
    b_str = int(b) if b == int(b) else b
    result_str = int(result) if result == int(result) else result
    
    return f"Result: {a_str} {symbol} {b_str} = {result_str}"


def main():
    """Main calculator loop."""
    display_welcome()
    
    while True:
        # Get first number
        a = get_number("Enter first number: ")
        if a is None:
            print("Goodbye!")
            break
        
        # Get operation
        operation = get_operation()
        if operation is None:
            print("Goodbye!")
            break
        
        # Get second number
        b = get_number("Enter second number: ")
        if b is None:
            print("Goodbye!")
            break
        
        # Calculate and display result
        print(calculate(a, operation, b))
        print()


if __name__ == "__main__":
    main()
