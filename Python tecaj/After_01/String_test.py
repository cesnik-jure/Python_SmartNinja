# Multiline text:
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to\
     """)

print("----------")

# Use "r" before string to disable \ functions:
print('C:\some\name')  # note the r before the quote
print(r'C:\some\name')  # note the r before the quote

print("----------")

# Use the "%" operator as argument specifiers ("%s" and "%d"):
in_num = input("Input: ")
print("Your input was: %s" % in_num)

print("----------")

# The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:
max = float(input("Max number for sequence: "))
a, b = 0, 1
while a < max:
    c = a
    a, b = b, a+b
    if a < max:
        print(c, end=',')
    else:
        print(c)

print("----------")
