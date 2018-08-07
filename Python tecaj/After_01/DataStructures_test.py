""" LISTS:
    - mutable
    - can include duplicates
"""
# An example that uses most of the list methods:
fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits)

print(fruits.count('apple'))
print(fruits.count('tangerine'))
print(fruits.index('banana'))

print(fruits.index('banana', 4))  # Find next banana starting a position 4

fruits.reverse()
print(fruits)

fruits.append('grape')
print(fruits)

fruits.sort()
print(fruits)

print(fruits.pop())
print(fruits)

a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)

del a[2:4]
print(a)

del a[:]
print(a)

# Looping through lists:
questions = ['name', 'quest', 'favorite color']
answers = ['Lancelot', 'the Holy Grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))


print("-"*40)
""" TUPLES:
    - immutable
    - can include duplicates
"""
t = 12345, 54321, 'hello!'
print(t[0])
print(t)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u

# Tuples are immutable:
#t[0] = 88888
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#TypeError: 'tuple' object does not support item assignment

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
print(v)

print("-"*40)
""" SETS:
    - mutable
    - cannot include duplicates
"""
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
print('orange' in basket)          # fast membership testing
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # unique letters in a
print(a - b)                              # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b)                              # letters in a or b but not both

print("-"*40)
""" DICTIONARIES:
    - mutable
    - can include duplicates
    - include pairs
"""
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
print(tel['jack'])

del tel['sape']
tel['irv'] = 4127

print(tel)
print(list(tel))
print(sorted(tel))

print('guido' in tel)
print('jack' not in tel)


# Looping through dictionaries:
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)


# Comparison of sequences:
print((1, 2, 3)              < (1, 2, 4))
print([1, 2, 3]              < [1, 2, 4])
print('ABC' < 'C' < 'Pascal' < 'Python')
print((1, 2, 3, 4)           < (1, 2, 4))
print((1, 2)                 < (1, 2, -1))
print((1, 2, 3)             == (1.0, 2.0, 3.0))
print((1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4))
