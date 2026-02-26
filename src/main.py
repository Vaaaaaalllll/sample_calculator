# WARNING: template code, may need edits
"""Command-line interface for the calculator."""

from src.calculator import Calculator


def print_menu():
    """Display the calculator menu."""
    print("\n=== Simple Calculator ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. View History")
    print("6. Clear History")
    print("7. Exit")
    print("=========================")


def get_numbers():
    """Get two numbers from user input.
    
    Returns:
        Tuple of two numbers
    """
    while True:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            return a, b
        except ValueError:
            print("Invalid input. Please enter valid numbers.")


def main():
    """Main function to run the calculator CLI."""
    calc = Calculator()
    
    # Demonstrate initial example: 1 + 1 = 2
    print("\nWelcome! Here's a quick example:")
    result = calc.add(1, 1)
    print(f"1 + 1 = {result}")
    
    while True:
        print_menu()
        choice = input("\nSelect an operation (1-7): ").strip()
        
        if choice == "7":
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice == "5":
            history = calc.get_history()
            if history:
                print("\nCalculation History:")
                for i, operation in enumerate(history, 1):
                    print(f"{i}. {operation}")
            else:
                print("\nNo history available.")
            continue
        
        if choice == "6":
            calc.clear_history()
            print("\nHistory cleared.")
            continue
        
        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select 1-7.")
            continue
        
        a, b = get_numbers()
        
        try:
            if choice == "1":
                result = calc.add(a, b)
                print(f"\nResult: {a} + {b} = {result}")
            elif choice == "2":
                result = calc.subtract(a, b)
                print(f"\nResult: {a} - {b} = {result}")
            elif choice == "3":
                result = calc.multiply(a, b)
                print(f"\nResult: {a} * {b} = {result}")
            elif choice == "4":
                result = calc.divide(a, b)
                print(f"\nResult: {a} / {b} = {result}")
        except ValueError as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()
