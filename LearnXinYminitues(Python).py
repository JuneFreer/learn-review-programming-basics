#Single line comments starts with a number symbol.

""" Multiline strings can be written
    using three "s, and are often used
    as documentation.""""

#######################################################
## 1. Primitive Datatypes and Operators
#######################################################

# you have numbers
3 # => 3

# Math is what you would expect
1 + 1 # => 2
8 - 1 # => 7
10 * 2 # => 20
35 / 5 # => 7.0

# Results of integer division truncated dwon both for positive and negative.
5 // 3 # => 1
5.0 // 3.0 # => 1.0 # works on floats # too
-5 // 3 # => -2
-5.0 // 3.0 # -2.0

# The result of division is always a float
10.0 / 3 # 3.3333333333

# Modulo operation
7 % 3 # 1

# Exponentiation (x ** y, x to the ythe power)
2 ** 3 # 8

# Enforce percedence with paratheses
(1 + 3) * 2 # 8

# Boolean values are primitives(Note: the capitalization)
True
False

# negative with not
not True
not False

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False # False
False or True # True

# True and False are actually 1 and 0 but with different keywords
True + True # 2
True * 8 # 8
False - 5 # -5

# Comaparison Operators look at the numerical value of True and False
 0 == False # True
 1 == True # True
 2 == True # False
 -5 != False # True

 # using Boolean logical operators on ints casts them to booleans for evaluation,
 #but their non-cast value is returned
 # Don't mix up with bool(ints) and bitwise and /or(&,|)
 bool(0) # False
 bool(4) # True
 bool(-6) # True
 0 and 2 # 0
 -5 or 0 # -5

 # Equality
 1 == 1 # True
 2 == 1 # False

 # inequality
 1 != 1 # False
 2 != 1 # True

 1 < 10 # True
 1 > 10 # False
 2 <= 2 #Ture
 2 >= 2 # True

 1 < 2 and 2 < 3
 2 < 3 and 3 < 2

1 < 2 < 3
2 < 3 < 2

a = [1, 2, 3, 4]
b = a
b is a
b == a
b = [1, 2, 3, 4]
b is a
b == a

# strings
"This is a string."
'This is also a string.'

"Hello " + "world!"
"Hello " "world!"

"This is a string"[0]

len("This is a string")

"{} can be {}".format("Strings", "interpolated")

"{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "Candle stick")

"{name} wants to eat {food}".format(name="Bob", food="lasagna")

# Python2.5 style
"%s can be %s the %s way" % ("String", "interpolated", "old")

name = "Reiko"
f"She said her name is {name}."

f"{name} is {len(name)} characters long."

# None is an object
None

"etc" is None #False
None is None #true

# None, 0, and empty strings/lists/dicts/tuples all evaluate to False.
# All other values are True
bool(0)
bool("")
bool([])
bool({})
bool(())

####################################################
## 2. Variables and Collections
####################################################

print("I'm python. Nice to meet you!")

print("Hello, world", end = "!")

input_string_var = input("Enter some data: ") #returns the inputs as a strings

some_var = 5
some_var
# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
some_unknown_var # NameError

#ternary operator
"yahoo!" if 3 > 2 else 2 #"Yahoo!"

li = []

other_li = [4, 5, 6]

li.append(1)
li.append(2)
li.append(4)
li.append(3)

li.pop()

li.append(3)

li[0]
li[-1]

li[4] # IndexError
# The start index is included, the end index is not
li[1:3] # [2, 4]

li[2:]

li[:3]

li[::2]

li[::-1]
# li[start:end:step]

li2 = li[:] # li2 == li, but li2 is not li

del li[2] # [2] is index

li.remove(2) # (2) is value
li.remove(2) # ValueError, 2 is not in the list

li.insert(1, 2) # 1 is index, 2 is value

li.index(2) # get the first index of value 2
li.index(4) # get the first index of value 4

li + other_li # add lists, returns a new list, li and other_li didn't changed

li.extend(other_li) # extend li, li changes

1 in li # True

len(li)

tup = (1, 2, 3)
tup[0] # 1
tup[0] = 3 # can not change values in tuple

type((1)) # <class 'int'>
type((1,)) # <class 'tuple'>
type(()) # <class 'tuple'>

len(tup)
tup + (4, 5, 6) # (1, 2, 3, 4, 5, 6)
tup[:2] # (1, 2)
2 in tup # True

# unpack tuples or lists
a, b, c = (1, 2, 3)

a, *b, c = (1, 2, 3, 4)

d, e, f = 4, 5, 6

# swap twoo values

e, d = d, e

# Dictionaries store mappings(映射) from keys to values
empty_dict = {}
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# 键必须是不可变的类型，来保证键可以被转换为常量哈希值
# Immutable types include ints, floats, strings, tuples.
invalid_dict = {[1,2,3]: "123"}  # TypeError: unhashable type: lists

valid_dict = {(1,2,3): [1,2,3]}

filled_dict["one"] # 1

list(filled_dict.keys()) # ["three", "two", "one"]

list(filled_dict.values())

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict # true
1 in filled_dict # False

filled_dict["four"] # KeyError

filled_dict.get("one") # 1
filled_dict.get("four") # None

# The get method supports a default argument when the value is missing
filled_dict.get("one", 4) # 1
filled_dict.get("four", 4) # 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5) # filled_dict["five"] == 5
filled_dict.setdefault("five", 6) # filled_dict["five"] == 5

filled_dict.update({"four": 4}) # one way Adding to a dictionary
filled_dict["four"] = 4 # another way

del filled_dict["one"] # {'three': 3, 'two': 2}

# sets
empty_set = set()
some_set = {1, 1, 2, 2, 3, 4} # some_set is now {1, 2, 3, 4}

# Similar to keys of a dictionary, elements of a set have to be immutable.
invalid_set = {[1], 1} # => Raises a TypeError: unhashable type: 'list'
valid_set = {(1,), 1}

filled_set = some_set
filled_set.add(5) # {1, 2, 3, 4, 5}
# Sets do not have duplicate elements
filled_set.add(5) # {1, 2, 3, 4, 5}

other_set = {3, 4, 5, 6}
filled_set & other_set #{3, 4, 5}

filled_set | other_set # {1, 2, 3, 4, 5, 6}

{1, 2, 3, 4} - {2, 3, 5} # {1, 4}
{1, 2, 3, 4} ^ {2, 3, 5} # 对称差 {1, 4, 5}
# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3} # False

{1, 2} <= {1, 2, 3} # true

2 in filled_set # true
10 in filled_set # False

####################################################
## 3. Control Flow and Iterables
####################################################

some_var = 5
# Here is an if statement. Indentation is significant in Python!
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:
    print("some_var is smaller than 10.")
else:
    print("some_var is indeed 10.")

"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    print("{} is a mammal".format(animal))

"""
"range(number)" returns an iterable of numbers
from zero to the given number
prints:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" returns an iterable of numbers
from the lower number to the upper number
prints:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

"""

While loops go until a condition is no longer met.
prints:
    0
    1
    2
    3
"""
x = 0
while x < 4:
    print(x)
    x += 1

# Handle exceptions with a try/except block
try:
    raise IndexError("This is an index error")
except IndexError as e:
    pass
except(TypeError, NameError):
    pass
else:
    print("all good!")
finally:
    print("We can clean up resources here")
