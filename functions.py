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

