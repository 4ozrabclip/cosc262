####QUESTION 1
# Write a function concat_list(strings) that takes a list of strings as a parameter and 
# returns a single string made up of all the individual strings in strings concatenated together, 
# in order. Your implementation must not use loops, the 'join' method of a string, or any imports. 
# Also (and this applies to all questions in this quiz unless otherwise specified) it shouldn't use 
# list comprehensions as they are loops in disguise, which do all the work for you!

# def concat_list(strings):
#     if len(strings) == 0:
#         return ""
#     return strings[0] + concat_list(strings[1:])

# ans = concat_list(['a', 'hot', 'day'])
# print(ans)

####QUESTION 2
# Write a function product(data) that returns the product of the elements in the list data, 
# or 1 if the list is empty. Your code must not use for or while, must not import anything and 
# must be pylint compliant except that docstrings are optional.

# def product(data):
#     return 1 if len(data) == 0 else data[0] * product(data[1:])

# print(product([1, 13, 9, -11]))

####QUESTION 3
# Write a function backwards(s) that returns its parameter string s in reverse. 
# Obviously you're not allowed to call the reverse method of the string nor the reversed function. 

# You also cannot use loops or use imports, and using slices with negative increments is cheating! 

# def backwards(s):
#     return "" if len(s) == 0 else s[-1] + backwards(s[:-1])


# print(backwards("Hi there!"))

####QUESTION 4
# Write a function odds(data) that takes a list of ints, data, as a parameter and returns a new list 
# that contains just the odd elements from data, i.e. those elements that are not exactly divisible by two. 
# Your code must not use for or while and must not import anything.


# def odds(data):
#     if len(data) == 0:
#         return []
    
#     if data[0] % 2 == 0:
#         return odds(data[1:])
#     return [data[0]] + odds(data[1:])

# print(odds([0, 1, 12, 13, 14, 9, -11, -20]))

####QUESTION 5
# Write a function squares(data) that takes a list of ints, data, as a parameter and returns a new list that contains the 
# squares of all the numbers in data. Your code must not use for or while, must not import anything and must be pylint compliant. 

# def squares(data):
#     return [] if len(data) == 0 else [data[0]**2] + squares(data[1:])

# print(squares([1, 13, 9, -11]))

####QUESTION 6
# Write a function find(data, value) that returns the subscript (position) of the first occurrence of value in data, 
# or None if the value is not found. Your function cannot use loops or list comprehensions and also cannot use the index method of a list.

# def find(data, value, i=0):
#     if len(data) == 0:
#         return None
    
#     elif value == data[0]:
#         return i
#     return find(data[1:], value, i+1)

# print(find(["hi", "there", "you", "there"], "there"))

####QUESTION 14.b

# Write an asymptotically most efficient implementation of the function almost_all(numbers) mentioned above.

# Note that while the above implementation produces the correct output, the time it requires to compute the output 
# grows too fast with respect to the size of the input (the length of the list numbers). 
# Your implementation must be such that a list of numbers with 105 elements can be processed in less than a second.

# def almost_all(numbers): 
#     m = sum(numbers)
#     return [m - x for x in numbers]


####QUESTION 15.a

# def foo(numbers): 
#     result = [] 
#     for i in range(len(numbers)): 
#         sub = sorted(numbers[i:]) 
#         result.append(sub[0]) 
#     return result

# The worst-case time complexity of this function is: O(n^2 log n)

# The worst-case time complexity of an asymptotically most efficient implementation of this function is: O(n)

####QUESTION 15.b
# Write an asymptotically most efficient implementation of the function foo(numbers) mentioned above. Your function must not modify the parameter numbers.

# Your implementation must be such that a list of numbers with 105 elements can be processed in less than a second.

# Hint: if your solution calls the sorted function or the sort method of a list, is it really going to have the right asymptotic complexity?

def foo(numbers): 
    if len(numbers) == 0:
        return []

    sorted_numbers = sorted(numbers)
    return [sorted_numbers[0]] + foo(sorted_numbers[1:])

foo(list(range(10**5)))
print("OK")

foo(list(range(10**5)))
print("OK")

	

# OK

	

# *** RUN TIME ERROR(S) ***
# Traceback (most recent call last):
#   File "__source.py", line 17, in <module>
#     foo(list(range(10**5)))
#   File "__source.py", line 6, in foo
#     return [sorted_numbers[0]] + foo(sorted_numbers[1:])
#   File "__source.py", line 6, in foo
#     return [sorted_numbers[0]] + foo(sorted_numbers[1:])
#   File "__source.py", line 6, in foo
#     return [sorted_numbers[0]] + foo(sorted_numbers[1:])
#   [Previous line repeated 941 more times]
#   File "__source.py", line 5, in foo
#     sorted_numbers = sorted(numbers)
# MemoryError