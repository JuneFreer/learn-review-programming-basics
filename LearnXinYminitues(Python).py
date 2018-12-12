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
