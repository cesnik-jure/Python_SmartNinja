# This is an example demonstrating how to reference the different scopes and namespaces, and how global and nonlocal affect variable binding:
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

print("-" * 40)

# Class for Complex numbers:
class Complex:
    """A simple example class for Complex number"""
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    class_attribute = 1111

# The call x.f() is exactly equivalent to MyClass.f(x).
    def f(self):
        return "Hello world"

# Create a new instance of the class and assign this object to the local variable x:
x = Complex(3.0, -4.5)
print("Documentaction:", x.__doc__)
print("Class Attribute:", x.class_attribute)
print("Class Method with arguments:","x =", x.r, "+", x.i, "i")
print("Class Method on self:", x.f())
