# Create a function that writes the Fibonacci series to an arbitrary boundary:
def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(float(input("Max number: ")))


# Test with local and global variables:
def test(p):
    a = p
    print("""\
p = %s
a = %s
""" % (p, a))

p = "Global P"
a = "Global A"
test(p)

print("""\
p = %s
a = %s
""" % (p, a))

# Return from function
def comeback(a,b):
    c = a + b
    return c

print(comeback(10,30))
