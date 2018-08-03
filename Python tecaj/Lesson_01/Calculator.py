# This is a comment.

firstNumber = float(input("Input first number: "))
secondNumber = float(input("Input second number: "))
operation = str(input("Input operation, use +, -, * or /: "))

# Test for operation.

if operation == "+":
    result = firstNumber + secondNumber
    print("Sum of both numbers is:", result)

elif operation == "-":
    result = firstNumber - secondNumber
    print("Difference of both numbers is:", result)

elif operation == "*":
    result = firstNumber * secondNumber
    print("Multiplication of both numbers is:", result)

elif operation == "/":
    result = firstNumber / secondNumber
    print("Division of both numbers is:", result)

else:
    print("Operation is not defined correctly!")
