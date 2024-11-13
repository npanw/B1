# write a program to create a list of squares of numbers from 1 to n using list compernsion ?

def list_of_squares(n):
    return [i**2 for i in range(1, n+1)]

n = 10
squares = list_of_squares(n)
print(squares)

# Write a program that use dictonery compernsion to create a dictonery where keys are number and values are square number ?

def dict_of_squares(n):
    return {i: i**2 for i in range(1, n+1)}

n = 10
squares_dict = dict_of_squares(n)
print(squares_dict)

# Write a function that takes a argumnet that is dictonery and returns where keys are value and values are keys ?

def invert_dict(d):
    return {v: k for k, v in d.items()}

original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = invert_dict(original_dict)
print(inverted_dict)

