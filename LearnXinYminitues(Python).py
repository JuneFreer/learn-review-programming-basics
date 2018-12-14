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

# Instead of try/finally to cleanup resources you can use a with statement
with open("myfile.txt") as f:
    for line in f:
        print(line)

# An iterable is an object that can be treated as a sequence.
filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)

# loop over it
for i in our_iterable:
    print(i)

# However we cannot address elements by index.
our_iterable[1]  # Raises a TypeError
#now our_iterable[1] can return 'two'

our_iterator = iter(our_iterable)

next(our_iterator) # 'one'
next(our_iterator) # 'two'
next(our_iterator) # 'three'

next(our_iterator) # Raises StopIteration

# You can grab all the elements of an iterator by calling list() on it.
list(filled_dict.keys())

####################################################
## 4. Functions
####################################################

# Use "def" to create new functions
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y
# Calling functions with parameters
add(5, 6) # prints out "x is 5 and y is 6" and returns 11
#keyword arguments
add(y = 6, x = 5)

def varargs(*args): #多个位置参数
    return args

varargs(1, 2, 3) # (1, 2, 3)

def keyword_args(**kwargs): # 多个关键字参数
    return kwargs

keyword_args(big = "foot", loch = "ness") # {"big": "foot", "loch": "ness"}

def all_the_args(*args, **kwargs): #同时
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

args= (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args) # equivalent to all_the_args(1, 2, 3, 4)
all_the_args(**kwargs) #equivalent to all_the_args(a=3, b=4)
all_the_args(*args, **kwargs) #equivalent to all_the_args(1, 2, 3, 4, a=3, b=4)

# Returning multiple values (with tuple assignments)
def swap(x, y):
    return y, x


x = 1
y = 2
x, y = swap(x, y) # x, y = y, x , x = 2, y = 1

# function scope
x = 5 # global var x
def set_x(num):
    x = num # local var x, x = arg num = 43
    print(x)

def set_global_x(num):
    global x # x = 5
    print(x)
    x = num # local var x, x = arg num = 6
    print(x)

set_x(43)
set_global_x(6)

# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder # 外层函数返回里层函数

add_10 = create_adder(10) #add_10 is adder(y): return 10 + y
add_10(3) # return 13

# There are also anonymous functions, 第二个括号是函数调用，括号里的是传递给函数的实参
(lambda x: x > 2)(3) # 3 > 2, True
(lambda x, y: x ** 2 + y ** 2)(2, 1) # 5

# There are built-in higher order functions
list(map(add_10, [1, 2, 3])) # 10+1, 10+2, 10+3 [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1])) # [4, 2, 3]
list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])) #[6, 7]

#List comprehension 列表综合式
[add_10(i) for i in [1, 2, 3]] # [11, 12 ,13]
[x for x in [3, 4, 5, 6, 7] if x > 5] # [6, 7]

#set and dict comprehensions
{x for x in 'abcddeef' if x not in 'abc'} #{'d', 'e', 'f'} set集合
{x: x**2 for x in range(5)} # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

####################################################
## 5. Modules
####################################################

import math
print(math.sqrt(16)) # 4.0

from math import ceil, floor
print(ceil(3.7)) # 4.0 向上取整
print(floor(3.7)) # 3.0 向下取整

# You can import all functions from a module.
# Warning: this is not recommended
from math import *

import math as m
math.sqrt(16) == m.sqrt(16)

# Python modules are just ordinary Python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.

# You can find out which functions and attributes
# are defined in a module.
import math
dir(math)

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.
#本地文件夹里的文件优先级高于内置python库

####################################################
## 6. Classes
####################################################
class Human:
    species = "H. sapiens   # A class attribute.
    def __init__(self, name):
        self.name = name
        self.age = 0 # Initialize property
    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name = self.name, message = msg))
    # Another instance method
    def sing(self):
        return "yo... yo... microphone check... one two... one two..."

    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference静态方法
    @staticmethod
    def grunt():
        return "*grunt*"
# A property is just like a getter.
# It turns the method age() into an read-only attribute of the same name.
# There's no need to write trivial(琐碎的) getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # a setter
    @age.setter
    def age(self, age):
        return self._age

    @age.deleter
    def age(self):
        def self._age

# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == '__main__':
    # Instaniate a class
    i = Human(name = "Ian")
    i.say("hi")
    j = Huam("Joel")
    j.say("hello")
    # call class method
    i.say(i.get_species())
    # set new attributes
    Human.species = "H. neanderhalensis"
    i.say(get_species())
    j.say(j.get_species())

    # call static method
    print(Human.grunt()) #"*grunt*"

# Cannot call static method with instance of object
# because i.grunt() will automatically put "self" (the object i) as an argument
    print(i.grunt()) # TypeError:grunt() takes 0 positional arguments but 1 was given
    # i.grunt() == grunt(i) i is self

    # Update the property(属性) for this instance
    i.age = 42
    i.say(i.age)
    j.say(j.age)
    del i.age # AttributeError

####################################################
## 6.1 Inheritance
####################################################

# human.py
from human import Human

class Superhero(Human):
    species = 'Superhuman'
    def __init__(self, name, movie = False, superpowers=["super strength", "bulletproofing"])
        # add additional class attributes
        self.fictional = True
        self.movie = movie
        self.superpowers = superpowers
        # The "super" function lets you access the parent class's methods
        super().__init__(name)

    # override the sing method
    def sing(self):
        return "Dun, dun, dun!"

    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))

if __name__ == '__main__':
    sup = Superhero(name = "trick")
    #Instancee type Check
    if isinstance(sup, Human):
        print("I am human")
    if type(sup) is Superhero:
        print('I am a superhero')

# get the method resolution search order used by bpth getattr() and super()
    print(Superhero.__mro__)
    print(sup.get_species())
    print(sup.sing())
    sup.say('spoon')
    sup.boast()
    sup.age =31
    print(sup.age)
    # Attribute that only exists within Superhero
    print("Am I oscar eligiable?" + str(sup.movie))

####################################################
## 6.2 Multiple Inheritance
####################################################

# Another class definition
# bat.py
