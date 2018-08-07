with open('workfile.txt', 'r+') as f:
    """read_data = f.read()
    print(read_data)"""

    for line in f:
        print(line, end='')
    # Move to the end of file:
    f.seek(0,2)
    f.write('This is a test\n')

print(f.closed)

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
