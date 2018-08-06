tax = 12.5 / 100
price = 100.50
price * tax
price += price*tax
print(round(price, 2))

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to\
     """)

print('C:\some\name')  # note the r before the quote
print(r'C:\some\name')  # note the r before the quote
