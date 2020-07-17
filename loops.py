'''
Python has two primitive loop commands 'while' and 'for'.
The while loop can execute a set of statements if the condition is true.
The while loop requires relevant variables to be ready beforehand.
A for loop is used for iterating over a sequence,
(that is either a list, a tuple, a dictionary, a set, or a string).
This is less like the for keyword in other programming languages,
and works more like an iterator method as found in other OOP languages.
With the for loop we can execute a set of statements,
once for each item in a list, tuple, set etc.
The for loop does not require an indexing variable to set beforehand.
Strings are iterable characters that contain a sequence of characters.
'''

'''
The range() function is used to loop through a set of code a specified
number of times. It returns a a sequence of numbers,
starting from 0 by default, and increments by 1 (by default),
and ends at a specified number. This is demonstrated here below:
'''
for x in range(5):
    print(x)
# Skipping a line.
print()
# Note that range(5) is not the values of 0 to 5, but the values 0 to 4.

'''
The range() function defaults to 0 as a starting value,
however it is possible to specify the starting value by adding a parameter:
range(1, 7), which means values from 1 to 7 (but not including 7):
This property of the range() function is demonstrated below:
'''
for y in range(1, 7):
    print(y)
# Skipping a line.
print()

'''
The range() function defaults to increment the sequence by 1,
however it is possible to specify the increment value by adding
a third parameter: range(3, 40, 5): This is demonstrated below:
'''
for z in range(3, 40, 5):
    print(z)
# Skipping a line.
print()

'''
In the code below the task is to print a string that has some message
a certain amount of times along with the number of times it was printed.
There will also be dot characters to indicate the number of times the
string message was printed out. There are several ways of doing this.
This will be done using a for loop along with the range function.
Here below is the first way to carry out the task:
'''
for i in range(5):
    # The print function takes the string called "message" as an argument.
    # Then it takes another argument that is i plus one. This is in order to
    # display the value of i based on the number of times message was printed.
    # If 1 was not added to i it would simply start by displaying 0 as a value.
    # Another argument is taken that adds i to 1 and multiplies it by the . string.
    # This displays dot characters equivalent to the number of times message is displayed.
    print("message", i + 1, (i + 1) * ".")
# Skipping a line.
print()


'''
In the range function we can add another parameter to show where
the value of i starts and where it ends. It starts from 1 up to but
not including 6. This means  it will iterate 5 times. This also allows
us to take out the + 1 which we had as shown in the code above.
'''
for i in range(1, 6):
    print("new message", i, i * ".")
# Skipping a line.
print()


# Another parameter is added to the range function that specifies the increment
# value for our for loop. It starts at 2 and is incremented by 4 until it reaches 24.
for i in range(2, 25, 4):
    print("new message", i, i * ".")
# Skipping a line.
print()


# The else keyword in a for loop specifies a block of code to be executed
# when the loop is finished: This is demonstrated in the example below.
for a in range(8):
    print(a)
else:
    print("Complete!")
# Skipping a line.
print()


# Declaring a boolean variable and assigning it the value of false.
success = False
# Using a for loop to iterate over the values in the range function.
for number in range(1, 6):
    # Printing a string along with the number of attempts.
    print("Attempt Number:", number)
    # If the boolean expression is true we break out of the loop and print a message.
    if success:
        print("Achieved!")
        break
# If the boolean expression is not true after iterating over each sequence
# of the for loop then we will execute the code in the else block.
else:
    # We print the amount of attempts and that we failed.
    print(f"Attempted {number} times and Failed.")
# Skipping a line.
print()

'''
In Python we have nested loops. It is essentially a loop inside another
loop. The "inner loop" will be executed one time for each iteration of the "outer loop":
In the example below we have two arrays that contain 3 elements.
The goal is to map one array element to another corresponding one.
'''

# Two array variables are declared with 3 elements.
adjective = ["Bounce", "Swing", "Throw"]
equipment = ["BasketBall", "Bat", "Baseball"]
# The outer loop iterates over the first array.
for c in adjective:
    # The inner loop iterates over the second array.
    for d in equipment:
        # The first element of the first array is printed
        # followed by the first element of the second array,
        # The inner loop is entered again until all the elements
        # of the inner loop have been iterated over and printed.
        # After that we return to the outer array and repeat the
        # same process until we have iterated over each element of
        # the outer loop and its corresponding inner loop element.
        print(c, d)
# Skipping a line.
print()


# The example below will use inner loops to display coordinates
# This will be done using formatted strings in our print line.
for e in range(3):
    for f in range(4):
        print(f"({e}, {f})")
# Skipping a line.
print()


# The range function is not the only type of object that is iterable.
# Lists and strings are also iterable. This is demonstrated below:
for word in "Programming":
    # The for loop iterates over each character in the string and prints it.
    print(word)
# Skipping a line.
print()


# We will use a while loop below to execute a statement if condition is true,
# We first define an indexing variable named value and set it to 1.
value = 1
# So long as the value is less than 5 then we will enter the loop.
while value < 5:
    # The value along with a string is printed upon each iteration.
    print("Value # ", value)
    value += 1
# A message is displayed once we have iterated over the entire loop.
print("Complete!")
# Skipping a line.
print()


# Below we have a while loop that takes user input and performs a certain
# operation. It terminates if the user decides to enter a certain value.
# We first define an indexing variable set to an empty string.
prompt = ""
# While the prompt variable is not equal to the string "quit" we enter the
# while loop. the prompt variable acceses the lower method to prevent an error.
# If the user enters quit with different cases (Upper & Lower) it would not work.
while prompt.lower() != "quit":
    # The prompt variable is assigned the input value read in by the user.
    prompt = input("Enter an expression: ")
    # The print line displays a string and the value read in by the user.
    print("Result: ", prompt)
# Skipping a line.
print()


# This program below displays the even numbers between 1 and 20.
# Then it tells us how many evn numbers we have in our range.
# We have a count indexing variable and set it equal to 0.
count = 0
# We iterate over the while loop from range 1 - 20.
for even in range(1, 20):
    # If our iterated values are even then we enter the if block.
    if even % 2 == 0:
        # The count indexing variable is incremented by 1.
        count += 1
        # The result of the even value is displayed.
        print(even)
# We then print how many even numbers we have in our range.
print(f"We have {count} numbers.")
