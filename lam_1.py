# Lamda functions!
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
