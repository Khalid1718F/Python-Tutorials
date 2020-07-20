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

'''

# We can access an item in a list by refering to its index position, demonstrated below:
fruit_list = ['apple', 'banana', 'cherry', 'orange',
              'kiwi', 'watermelon', 'grape', 'cantelope']
print(fruit_list[1])

# Negative index positions can also be used to refer to list items as shown below:
print(fruit_list[-1])  # Prints last item on a list.

'''
You can specify a range of indexes by specifying where to start and where to end the range.
When specifying a range, the return value will be a new list with the specified items.

'''
