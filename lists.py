'''
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and un-indexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

When choosing a collection type, it is useful to understand the properties of that type. 
Choosing the right type for a particular data set could mean retention of meaning, 
and, it could mean an increase in efficiency or security.

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
They are an aggregate data type which means that they are composed of other data types. 
for example you can have a list of strings, ints, floats, booleans, other list, and mixed types. 

'''


# Lists are indexed and have a length property that can count the number of items within them.
# We can access an item in a list by refering to its index position, demonstrated below:
fruit_list = ['apple', 'banana', 'cherry', 'orange',
              'kiwi', 'watermelon', 'grape', 'cantelope']
print(fruit_list[1])  # Prints second item on a list.

# Negative index positions can also be used to refer to list items as shown below:
print(fruit_list[-1])  # Prints last item on a list.

'''
We can check the length of a given list by using the len() function.
This function takes a list as an argument and returns the length of a list as an integer value.
An example of using this function is demonstrated below using the list above. 
'''
print(len(fruit_list))  # Prints the length of our list.

'''
Lists can also be sliced. The slicing operation always returns a new list 
that's been derived from the old list. The syntax remains as list[start_index : end_index]
'List Slicing' is also known as 'Range of Indexes' because it allows us to specify the range
based on where we would like it to start and where we would like it to end.
It is important to note that the element in the end index is not included in the new list. 
'''

# Here list slicing is demonstrated by printing the last four items of our list.
print(fruit_list[4:8])  # Prints the last four items on our list

# NOTE: There are different ways to perform the same task shown here below:

print(fruit_list[-4:])  # 1) Negative indexing
print(fruit_list[len(fruit_list) - 4:])  # 2) Using the len() function.
# Below when we omit the ending index, by default python will slice all the items
# from the starting index until the end index (The last element in the list)
print(fruit_list[4:])  # 3) Omitting the ending index.

# If we were to leave out the start value of a list object, the range will start at
# the first item by default (i.e Starting at index 0). Demonstrated below:
print(fruit_list[:4])  # Prints out the first four items of the list.

'''
We can also change the value of an item on a list by reffering to its index position. 
This can be done because lists are mutable Data Structures. This is demonstrated below,
where we change the value of the last item on a list using negative indexing. 
'''
fruit_list[-1] = 'Mango'  # changes the value of the last item in a list.
print(fruit_list)  # Will print the item in the new fruit_list object.

''' 
Note that it's possible to add any type of value to a list, 
regardless of what types of values it contains. 
This is possible through several methods.
'''
fruit_list.append('cantelope')  # 1) Adds an item to the end of a list.
fruit_list.insert(3, 'blueberry')  # 2) Adds an item to a specific index.
print(fruit_list)  # prints the new fruit list after changes have been made.
