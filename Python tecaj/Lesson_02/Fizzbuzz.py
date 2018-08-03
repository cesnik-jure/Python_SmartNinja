number1 = int(input("Input whole positive number as the first divider: "))
number2 = int(input("Input whole positive number as the second divider: "))
minimum = int(input("Select a whole number for the lower limit: "))
maximum = int(input("Select a whole number for the upper limit: "))

i = minimum

while i <= maximum:
    if i % number1 == 0 and i % number2 == 0:
        print("fizzbuzz")
    elif i % number1 == 0:
        print("fizz")
    elif i % number2 == 0:
        print("buzz")
    else:
        print(i)
    i += 1