# Below is an example of conditional statements in python.
# First we declare a variable and assign it a value.
temperature = 75
# The 'if' keyword is used along with a boolean expression.
# If the boolean is true, the code in the if block is executed.
if temperature == 75:
    print("It's a nice day today!")
# The elif block is executed if any of the conditional statements are true.
elif temperature > 75:
    print("It's kinda hot outside.")
elif temperature < 75:
    print("It's starting to get chilly outside.")
# If none of the conditional statements are true the else block is executed.
else:
    print("What's the temperature like outside?")
# This print statement is executed at the after the if-elif-else statements.
print("Finished!")
print("--------------------------------------------------------")

# Below is an example of a ternary operator.
# We declare a variable that we will use for our conditional statement.
age = 21
'''
Another variable is declared and is assigned a String value.
After the message variable we have an if statement followed
by a boolean expression. If the expression evaluates to true,
then the message variable will be assigned the first value.
Then we have an else statement followed by a String value.
If the statement is false then the message variable will be
assigned the value of the second String value.
message = "Eligible" if age >= 21 else "Ineligible"
The message variable is now printed based on the comparison.
'''
print(message)
print("--------------------------------------------------------")

# Below is an example of how to use logical operators
# In python there are 3 logical operators (and, or, & not).
# First we create two variables and assign them a boolean value.
firstVariable = True
secondVariable = False
# Now we use the and operator to compare our two boolean variables.
# When using the and both variables or expressions must be true.
if firstVariable and secondVariable:
    print("Our expression is true.")
# We add an else statement in case one of our variables is false.
else:
    print("Our expression is false.")
# We create two more variables to demonstrate the or operator.
thirdVariable = False
fourthVariable = True
if thirdVariable or fourthVariable:
    print("One of our expressions is true.")
# The not operator reverses the value of any boolean variable or expression.
if not thirdVariable:
    print("We reversed our expression.")
# Below we will use all three operators in a single statement.
if (firstVariable or secondVariable) and not thirdVariable:
    print("We have used all three logical operators.")
print("--------------------------------------------------------")

# We can also chain comparison operataors in python by writing the expression.
value = 15
if 10 <= value < 20:
    print("We have used comparison operators by chaining them.")
