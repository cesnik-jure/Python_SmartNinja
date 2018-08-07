""" Import a module:"""
import fibo

fibo.fib1(1000)
print(fibo.fib2(100))
print(fibo.__name__)

""" Import specific functions and rename them, but not module:
from fibo import fib as fibonacci
fibonacci(500)
"""

""" Import all functions, but not module:
from fibo import *
fib(500)
"""

# Default paths to search for modules and adding another path to them:
import sys
def write_paths():
    for one_path in sys.path:
        print(one_path)

write_paths()

sys.path.append('/ufs/guido/lib/python')
write_paths()

print(dir(fibo))
print(dir(sys))
