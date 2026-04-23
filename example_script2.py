#!/usr/bin/env python3
"""
Simple Python example script demonstrating basic functionality.
This script reads a file, processes data, and outputs results.
"""

def fibonacci(n):
    """Generate Fibonacci sequence up to n numbers."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def calculate_average(numbers):
    """Calculate average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def greet(name, greeting="Hello"):
    """Return a greeting message."""
    return f"{greeting}, {name}!"


def main():
    """Main function to demonstrate the script's capabilities."""
    print("=" * 50)
    print("Python Example Script")
    print("=" * 50)
    
    # Example 1: Fibonacci sequence
    print("\n[Example 1] Fibonacci Sequence (first 10 numbers):")
    fib = fibonacci(10)
    print(fib)
    
    # Example 2: Average calculation
    print("\n[Example 2] Average of numbers:")
    numbers = [10, 20, 30, 40, 50]
    avg = calculate_average(numbers)
    print(f"Numbers: {numbers}")
    print(f"Average: {avg}")
    
    # Example 3: Greeting
    print("\n[Example 3] Greeting:")
    print(greet("World", "Hi"))
    
    print("\n" + "=" * 50)
    print("Script completed successfully!")
    print("=" * 50)


if __name__ == "__main__":
    main()
