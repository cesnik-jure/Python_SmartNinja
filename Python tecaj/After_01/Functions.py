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
def comeback(a, b):
    c = a + b
    return c

print(comeback(10,30))

# The following function accumulates the arguments passed to it on subsequent calls:
def f(a = 4, L = []):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f())

# Functions can also be called using keyword arguments:
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# A final formal parameter *name receives a list and **name receives a dictionary:
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "Yes, quite runny.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch",
           show="Monty Python's Flying Circus")
