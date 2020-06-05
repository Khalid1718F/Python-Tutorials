# This is a simple String variable that is stored in double quotes.
# We can also use single quotes if we wanted but it is better to use double.
course = "Python Programming!"
# This is an example of a multi-line String.
# We use three double quotes to open and close a multi-line String.
message = """
I am using,
a multi-line string,
so I can separate the lines.
"""
# We use the len function to get the length of the String that
# is passed as the argument. Here the argument is the message variable.
print(len(message))
# Here we get the first character in the String by entering the index position.
print(course[0])
# Here we get the last character in the String by entering -1 as the index position.
print(course[-1])
# Here we return the first three characters in the string by indicating the index.
# We use the first index position followed by a colon & then the third index position.
# This means that the print line will return the characters from,
# index 0 up to but not including index 3.
print(course[0:3])

# Here we demonstrate how to use escape sequences in Strings.
# We can put a backslash character whenever we encounter a single or double quote.
# We can also put two backslashes if we want the string to show a backslash character.
# If we put \n then it will take us to a new line & \t is a new tab.
escape = "This \"is how to use, \nan escape sequence to get quotes and a new line!\""
print(escape)

# Here we demo how to use formatted Strings.
# If we wanted to concatenate two string variables we can do this.
first = "Khalid"
last = "Ahmed"
full = first + " " + last
print(full)

# We can use another approach to format these two strings.
# We can set the variable full to a String that is prefixed with an 'F'
# The 'F' which stands for format can be upper or lowercase.
# Inside the string we put our two variables that we format in curly braces.
# This formatted string doesn't have a constant value like the first 2 strings.
# It is actually an expression that will be evaluated at run-time.
# You can put any valid expression in between the curly braces.
full = F"{first} {last}"
print(full)

# Here we will demo how to use String Methods in order to manipulate strings.
# When we use the dot operator '.' after our string variable,
# We get access to all the string methods of that variable.
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("Pro"))
print(course.replace("p", "j"))
# Checks to see if these chars exist in original string.
print("Pro" in course)
# returns boolean if char is not in original string.
print("Swift" not in course)