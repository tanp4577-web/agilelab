import sys
from app.calculator import add, subtract, multiply, divide

def menu():
    print("\n--- Menu-Driven Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = input("Enter choice (1-5): ")
    if choice == '5':
        print("Goodbye!")
        sys.exit(0)
        
    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"Result: {divide(num1, num2)}")
                except ValueError as e:
                    print(e)
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        menu()
