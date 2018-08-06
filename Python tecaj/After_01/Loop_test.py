# Searching for prime numbers:
"""prime_list = []

for n in range(2, 10000):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        prime_list.append(n)
        print(n, 'is a prime number')

print(prime_list)
print(len(prime_list))
"""

# Check if one of:
a = [1,2,3]
if int(input("Num: ")) in a:
    print("OK")
else:
    print("NOT OK")
