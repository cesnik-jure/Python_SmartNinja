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

yes_votes = 42_572_654 ; no_votes = 43_132_495
percentage = yes_votes/(yes_votes+no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

print("----------")
# Other string input methods:
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

dictionary = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(dictionary))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
