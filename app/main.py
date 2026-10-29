import sys

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def menu():
    print("\n--- Menu-Driven Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Exit")
    
    choice = input("Enter choice (1-3): ")
    if choice == '3':
        print("Goodbye!")
        sys.exit(0)
        
    if choice in ['1', '2']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    while True:
        menu()
