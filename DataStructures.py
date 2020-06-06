# There are four collection data types in the Python programming language:
# 1) List is ordered & changeable. Allows duplicate members.
# 2) Tuple is ordered & unchangeable. Allows duplicate members.
# 3) Set is unordered & un-indexed. No duplicate members.
# 4) Dictionary is unordered, changeable & indexed. No duplicate members.
# All of these collections are objects & can access their respective methods.
# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon,
# meaning that you can traverse through all the values.
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:
# Even strings are iterable objects, and can return an iterator:
# This is because a string is a sequence of characters.


# Here we create a list of languages and then display all the elements.
languages = ["English", "Spanish", "Arabic", "French", "Italian"]
print(languages)

# A Single item in a list can be accessed by referring to it's index.
print(languages[3])

# Negative indexing can be used to access items from a list in reverse.
print(languages[-1])

# The range of indexes in the items of a list can be accessed by
# specifying the range using the ':' where we place the starting
# value before the : and place the value up to but not including
# the value that we are trying to reach in our list.
print(languages[1:4])

# By leaving out the start value, the range will start at the first item:
print(languages[:4])

# By leaving out the end value, the range will go on to the end of the list:
print(languages[2:])

# We can also add a step to get items by moving over the desired number
# of index positions in our list. This is done by using two colons in []
# This is useful in situations where we want to skip over items in the list.
print(languages[::2])


# To change the value of a specific item, refer to the index number:
languages[2] = "Japanese"
print(languages)

# Lists can have objects of different types: (Strings, numbers, booleans, lists)
# Below is an example of a list that contains objects of different data types:
mixedList = ["Mixed", [0, 1, 2, 3, 4, 5, 6, 7], True, 25, 12.7]
print(mixedList)

# Below is a list within another list, so each item will be another list.
# This type of a list is known as a two dimensional matrix.
matrix = [[0, 0], [1, 1], [2, 2], [3, 3]]
print(matrix)

# We can also perform operations on lists and the elements within them.
# Suppose you want a list of 50 ones, you can multiply the list by 50.
ones = [1]*50
print(ones)

# Lists of different types can also be joined together using the '+' operator.
strings = ["This", "is", "a", "string", "list", "!"]
numbers = [2, 4, 6, 8]
joinedList = strings + numbers
print(joinedList)

# There may be times where we would like to take individual items from a list,
# and assign them to variables. This could be done by acessing each element in
# the list individually by its index and then assigning it to a variable.
# There is a cleaner way to do it which is called list unpacking.
# Below is a demonstration of unpacking a list into multiple variables.
# We will declare our variables in order seperated by a comma and then
# assign the value of our numbers list that we created above.
two, four, six, eight = numbers
print(two, four, six, eight)

# If there is a list that contains many items and we only want to store
# the values of a certain amount of items then we can pack the rest of
# the items that we are trying to retrieve in a single variable using '*'
# This example below demonstrates how to pack excess items in another variable.
# We will use our strings list to store the first two words and pack the rest.
wordOne, wordTwo, *otherWords = strings
print(wordOne, wordTwo)
print(otherWords)

# If we only want access to the first and last item in a list we can change
# the placement of our *other variable to the middle of the list & print them.
# We will use our same strings list to demonstrate this implementation.
firstWord, *otherWords, lastWord, = strings
print(firstWord, lastWord)
print(otherWords)

# It is also possible to use the list() constructor to make a new list.
# The range function is used within the list function to create a list
# in the code below by passing a value inside the range function.
# The range function will iterate over the values and the list function
# will take those iterated values and turn them into elements in a list.
iterable = list(range(1, 11))
print(iterable)

# The list function takes iterable values and such as strings and turns
# each character in the list into an item in the new list variable
characters = list("Learning Python!")
print(characters)

# The length of a list can be found using the len() function:
print(len(characters))

# We can also loop over our items in a list using a for loop shown below.
for chars in characters:
    print(chars)

# In order to get the index of each item in the list we can use a built in
# python function called enumerate() which will return an enumerate object
# This is an object which is iterable. In each iteration the enumerate object
# will give us a tuple. That contains the index of the item followed by the
# value of the item. This tuple is read only and we cannot add new items to it.
# In this example we will use our languages list and unpack the values
# into two variables one for index and one for the language item. The unpacking
# will take place within the for loop and we will print the index & value.
for index, language in enumerate(languages):
    print(index, language)

# We can also add items to a list using different techniques.
# The append() method is used to add an item to the end of a list.
# The insert() method is used to add an item to a specific index of a list.
# Both methods will be demonstrated here using our languages list:
languages.append("Arabic")
languages.insert(0, "Korean")
print(languages)

# There are several methods to remove items from a list:
# The remove() method removes the specified item:
# If there are multiple occurrences of an item it
# will remove the first occurrence of that item.
languages.remove("Korean")
# The pop() method removes the specified index,
languages.pop(0)
# (or the last item if index is not specified):
languages.pop()
# The del keyword removes the specified index or a range:
# The del keyword can also delete the list completely:
del languages[0:2]
print(languages)
# The clear() method empties the list:
languages.clear()
print(languages)

# There are also different techniques for finding items in a list.
letters = ["A", "B", "C", "C", "C"]
# We can use an if statement to check if an item exists in a list.
# We can also use the index() method to find index of an item:
# The index() method will return the first occurrance of that item:
if "C" in letters:
    print(letters.index("C"))

# We also have another method called count() which returns the
# number of occurrence of a given item in a list.
print(letters.count("C"))

# Lists can also be sorted in several different ways.
mixedValues = [70, 181, 2, 33, 28, 18, 1]
# We have a built in function called sorted that takes in an
# iterable as well as a key & reverse parameter.
# The sorted method will return a new sorted list:
print(sorted(mixedValues))
print(sorted(mixedValues, reverse=True))
# We can take a list of unsorted items and sort them in
# ascending or decending order using the sort() method.
# This method takes in two parameters (key, reverse).
# The sort method modifies our original list:
# This sorts a list in ascending order.
mixedValues.sort()
print(mixedValues)
# This sorts a list in decending order by using the reverse
# parameter in the sort() method and setting it to True.
mixedValues.sort(reverse=True)
print(mixedValues)


# Suppose that we have a situation where we have a list of items that
# are grouped as tuples with 2 items such as products and their price.
# What if we want to sort these items by their price? Python will not
# be able to sort such a list because there is no clear way on how
# to sort the items. In this situation we need to define an function
# that python will use for sorting lists. We will sort the items
# from most expensive to least expensive. Decending order.
products = [
    ("iPhone", 700),
    ("Airpods", 200),
    ("MacBook", 2500),
    ("Charger", 30),
    ("Apple Watch", 300)
]

# Here we define a function that will sort the products.
# This function will take in products as the parameter &
# will return a value that will be used for sorting items.
# In this case the function will return the price of the
# product in the the tuple. This allows python to deal with
# a list of numbers and it can easily sort the items in products.


def sortProducts(products):
    return products[1]

# Now we pass our sorting function as a key parameter in the
# in the sort() method which will be accessed by the products.
# NOTE: We are not caling the function but rather calling a
# reference to the function, hence we don't use parenthesis.
# We must use keyword arguments when calling the function
# so that we avoid getting a TypeError due to lack of positional
# arguments. So we must set the function we defined to key.


products.sort(key=sortProducts, reverse=True)
print(products)

# There is a much cleaner way of solving the problem above.
# We can use what is known as a lambda expression.
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments,
# but can only have one expression. Use lambda functions
# when an anonymous function is required for a short period of time.
# The syntax for using lambda is as follows:
# (key = lambda parameters/arguments : expression)
# By using the lambda function we no longer have to define a function
# to sort the items in our products list. So we can assign lambda to
# the key in our positional arguments for our sort method.
products.sort(key=lambda products: products[1])
print(products)


# Suppose that we want to extract only the price of the items
# in our products list and turn it into a list of prices.
# We can use the built in map() function along with a
# lambda expression and a the list constructor to do this.
# The map() function takes in 2 parameters a function and
# one or more iterables. The map() function will apply the
# lambda function on each item in this list. The lambda function
# will taransform each item in our original list. The parameter
# to the lambda function will be the product and the return value
# will be the price of the product which is product[1]. The second
# argument to our map function will be our entire products list.
# The products list is our iterable parameter. The map function will
# iterate over the products iterable and will call the lambda
# function on each item of this iterable which is our products list.
# The map function will return a map object which is another iterable
# that we can iterate over using a for loop or we can convert this
# map object into a list object and store the value in a variable.
price = list(map(lambda product: product[1], products))
print(price)

# This is the other way of displating prices with a for loop:
prices = map(lambda product: product[1], products)
for product in prices:
    print(f"This product costs {product}$ ")

# There is another built in Python function called filter()
# This function take in two parameters similar to the map() function:
# It takes a function or a None object and an iterable.
# The function will by applied on each item of the iterable.
# If the item matches some criteria it will return it.
# In this example we want to check if there are any items in our list
# that are less than or equal to 500 dollars. If such items exist then
# we want to display those items. The items will be stored in a variable.

productName = filter(lambda product: product[1] <= 500, products)
for product in productName:
    print(f"{product} is less than 500$.")

