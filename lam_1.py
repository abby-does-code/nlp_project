# Lamda functions! #
## Can take any number of arguments, but only one expression.
##Lamda function returns a function object
##You can only have one expression, but as many arguments as you want!


remainder = lambda num: num % 2

# print(remainder(5))
# OUTPUT: 1

product = lambda x, y: x * y

# print(product(2, 3))
# OUTPUT: 6


def testfunc(num):
    print(num)
    return lambda x: x * num


result1 = testfunc(10)
result2 = testfunc(100)

print(result1(9))
print(result2(9))

"""OUTPUT: 
10
100
90
900"""

# Making a change

# Applying given fucntion to each item of a given iterable

# Return double of n
def addition(n):
    return n + n


# Double all numbers using regular function

numbers = (1, 2, 3, 4)
result = map(addition, numbers)

print(list(result))  # We use this list command to filter results as a list

# OUTPUT: [2, 4, 6, 8]

# The same thing using lambda2 variable
numbers = (1, 2, 3, 4)
numbers2 = (5, 6, 7, 8)

result = list(map(lambda x, y: x + y, numbers, numbers2))

print(result)
# OUTPUT: [6, 8, 10, 12]

# You can have as many arguments as you wan,t but only one function!
