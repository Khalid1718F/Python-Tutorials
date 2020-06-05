# This program demos the popular FizzBuzz algorithm.
# The rules for this challenge is as follows:
# Create a function that reads input from the user.
# 1) If the input is divisible by 3 it will return "Fizz"
# 2) If the input is divisible by 5 it will return "Buzz"
# 3) If the input is divisible by 3 & 5 it will return "FizzBuzz"
# 4) If the input is not divisible by 3 or 5 then it will return
#    the value that was entered by the user on the console.


def fizz_buzz(value):
    if (value % 3 == 0) and (value % 5) == 0:
        return "FizzBuzz"
    if value % 3 == 0:
        return "Fizz"
    if value % 5==0:
        return "Buzz" 
    return value


print(fizz_buzz(22))
