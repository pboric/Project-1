from calculator.calculator import Calculator

def main():
    # Create a Calculator object
    calc = Calculator()

    # Ask the user for the first input
    num1 = float(input("Enter the first number: "))

    # Ask the user for the operation
    operation = input("Enter the operation (+, -, *, /, root): ")

    # Perform the operation
    if operation == "root":
        n = float(input("Enter the degree of the root: "))
        calc.add(num1)  # Update the memory value to num1
        result = calc.root(n)
    else:
        # Perform addition with the first input
        calc.add(num1)

        # Ask the user for the second input
        num2 = float(input("Enter the second number: "))

        if operation == "+":
            result = calc.add(num2)
        elif operation == "-":
            result = calc.subtract(num2)
        elif operation == "*":
            result = calc.multiply(num2)
        elif operation == "/":
            result = calc.divide(num2)
        else:
            print("Invalid operation")
            return

    # Print the result
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
