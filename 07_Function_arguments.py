# def sum(a, b):
#     return a + b

# def sum1(a, /, b):  # a is a positional-only parameter
#     return a + b

# def sum2(a, *, b):  # b is a keyword-only parameter
#     return a + b

# print(sum(3, 5))        # Both arguments can be positional or keyword
# print(sum(a=3, b=5))    # Both arguments can be positional or keyword

# print(sum1(3, 5))       # a must be positional, b can be positional
# # print(sum1(a=3, b=5)) # This would raise a TypeError

# print(sum2(3, b=5))     # a can be positional, b must be keyword
# # print(sum2(a=3, 5))   # This would raise a TypeError

from operator import add


def sum_all(*args):  # Accepts any number of positional arguments, stored as a tuple
    total = 0
    print(type(args))  # <class 'tuple'>
    print(args)       
    for num in args:
        total += num
    return total

def sum_all_kwargs(**kwargs):  # Accepts any number of keyword arguments, stored as a dictionary
    total = 0
    print(type(kwargs))  # <class 'dict'>
    print(kwargs)      
    for num in kwargs.values():
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # Outputs: 15
print(sum_all_kwargs(a=1, b=2, c=3))  # Outputs: 6


def mixed_args(a, b, /, c, *, d): # a and b are positional-only, c is positional or keyword, d is keyword-only
    return a + b + c + d

print(mixed_args(1, 2, 3, d=4))  # Valid call
# print(mixed_args(a=1, b=2, c=3, d=4))  # This would raise a TypeError


#You can use both *args and **kwargs in the same function.

# The order must be:

# regular parameters
# *args
# **kwargs

def combined_example(x, y, /, *args, z=0, **kwargs):
    print(f"x: {x}, y: {y}")
    print(f"args: {args}")
    print(f"z: {z}")
    print(f"kwargs: {kwargs}")

combined_example(1, 2, 3, 4, 5, z=10, a=100, b=200)


# unpacking arguments with * and **

def sum_three(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(sum_three(*numbers))  # Unpacking list

def info(name, age, adult):
    return name, age, adult

dict = {'name': 'Alice', 'age': 30, 'adult': True}
print(info(**dict))  # Unpacking dictionary


# lambda functions (anyonymous functions)
#A lambda function can take any number of arguments, but can only have one expression.


# lambda arguments : expression

add = lambda x, y: x * y
print(add(3, 5)) 

# double = lambda x: x * 2
# print(double(7))  # Outputs: 14

def double_func(n):
    return lambda x: x * n

double=double_func(5)       #the double will now became a function look like this lambda x: x * 5.
print(double(7))  # Outputs: 35