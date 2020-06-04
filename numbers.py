# Here we import the math module in order to work with numbers more.
# A module is a separate file with some python code.
# The math module comes with lots of math functions to work with numbers.
# In this program math is an object that access the methods of the module.
import math

# In python there are 3 types of numbers.
# We have integers, floats, and complex numbers.
# A complex number in math takes the form a + bi.
# In programming we replace the 'i' with a 'j'.
x = 1
y = 1.3
z = 1 + 3j

#  We also have standard math operations.
print(3 + 4)
print(3 - 2)
print(3 * 3)
# This sort of division yields a floating point number.
print(3 / 9)
# Division with two slashes yields an integer value.
print(9 // 4)
print(10 % 3)
# We also have exponents where left is to the power of right.
print(3 ** 3)

# We also have augmented assignment operators to increment & decrement val.
x = 20
x += 10
print(x)

# Here we have some useful functions for working with numbers.
# Below we have several built in functions like round and abs.
print(round(9.8))
print(abs(-3.7))

# We use the math.ceil() method to get the next highest whole number.
print(math.ceil(3.1))

# We have a built in function that takes input from the user.
# We store the value in a variable and create another variable to add 3 to it.
a = input("a: ")
# Here we have to typecast the value of a because it is a string.
b = int(a) + 3
# We format a & b so that we can display our output on the terminal.
print(f"a: {a}, b: {b}")

# This function returns the type of the variable that is passed as an argument.
print(type(a))
