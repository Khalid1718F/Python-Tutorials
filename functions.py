# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# In Python a function is defined using the def keyword:
# See the example below:


def myFunction():
    print("This is a function")


# Here we call our function below.
myFunction()
print()

# Information can be passed into functions as arguments.
# Arguments are specified after the function name,
# inside the parentheses. You can add as many arguments as you want,
# just separate them with a comma.
# The terms parameter and argument can be used for the same thing:
# information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.
# By default, a function must be called with the correct number of arguments.
# Meaning that if your function expects 2 arguments,
# you have to call the function with 2 arguments, not more, and not less.


def nameFunction(first, last):
    print("What's your full name?")
    print(f"{first} {last}")


# Function takes in two arguments and is called.
nameFunction("John", "Doe")
print()

# There are 2 types of functions in Python:
# 1) Functions who return a value.
# 2) Functions who perform a task.\
# Another function is defined and passed the same parameters.


def greetingFunction(first, last):
    # It returns the value of a formatted string.
    return f"Hello my name is {first} {last}!"


# The function is called an stored in a variable that is printed.
greeting = greetingFunction("John", "Doe")
print(greeting)
print()

# We can define an function that takes in a variable number of args.
# The number of parameters usually have have to equal the number of args.
# If they are not equal then we will get an error and must rewrite it.
# To solve this problem we can use the '*' symbol before the parameter.
# The function receives a tuple of arguments, and can access the items accordingly:
# Below is an example of a function the uses the '*' for multiple args.
# This example will define a function that takes in multiple arguments
# and will display the value of only a single argument.


def guess(*letter):
    print("What letter am I thinking of? ")
    print("I think it's", letter[2])


guess("A", "B", "C", "D", "E")
print()

# If you do not know how many keyword arguments that will be passed
# into your function, add two asterisk: ** before the parameter name
# in the function definition.This way the function will receive a
# dictionary of arguments, and can access the items accordingly:
# You can also send arguments with the key = value syntax.
# In this example we will display be able to save and access
# customer information usingkey word args while only having 1 parameter.


def customerInfo(**info):
    # key valued are accessed using [] & inside "" along with the parameter.
    print("How old are you? ")
    print("I am", info["age"])
    print("What's your ID number?")
    print("My number is", info["number"])
    print("What's your credit score?")
    print("My score is", info["credit"])


# We call the method where it contains all the keys & values within the args.
customerInfo(age=28, number=12345, credit=745)
print()

# A variable is only available from inside the region it is created.
# This is called scope. A variable created inside a function belongs to
# the local scope of that function, and can only be used inside that function.
# A variable created in the main body of the Python code is a global variable
# and belongs to the global scope. Global variables are available from within
# any scope, global and local. If you operate with the same variable name inside
# and outside of a function, Python will treat them as two separate variables,
# one available in the global scope (outside the function) and one available
# in the local scope (inside the function): The example below will declare two
# variables that have the same name. One is local and one is global.
# After declaring them they will both be displayed and the difference will be seen.

variable = 10


def localVariable(variable):
    variable = 20
    return variable


print(localVariable(localVariable))
print(variable)
