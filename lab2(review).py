#### QUESTION 1
# For a positive n, the Collatz sequence-length of n is the number of numbers generated in the 
# Collatz sequence starting from n up to 1 (including n and 1). In the example above, the sequence length of 22 is 16.

# Write a recursive function sequence_length(n) to compute the Collatz sequence length of a the given positive integer. 
# You are not allowed to import any module or use any types of loop (for, while, list comprehension, ...).

# def sequence_length(n):
#     if n <= 1:
#         return 1
#     elif n % 2 == 0:
#         return 1 + sequence_length(n/2)
#     return 1 + sequence_length((3*n+1))

# print(sequence_length(22))


####QUESTION 2
# Write a recursive function recursive_divide(x, y) to perform integer division without any of the following:

#     importing a module
#     using operators *, /, //, or %
#     using any types of loop (for, while, list comprehension, ...)

# The function must return what x//y would return in Python 3. Assume x >= 0 and y > 0 is true.

# def recursive_divide(x, y):
#     if x < y:
#         return 0
#     return 1 + recursive_divide(x-y, y)

# print(recursive_divide(9, 3))

####QUESTION 3
# The recursive function dumbo_func, which has been preloaded into the answer box, has O(n2) performance. 
# Rewrite it (still using recursion) so that its performance becomes O(n). 
# Your function will be tested in a loop calling it 20 times with a list of up to 10,000 elements and will time out if the function is still O(n2 ).

# Note that the function is preceded by code to increase the maximum recursion depth. 
# You will need to include that code when doing your own testing and when submitting your answer. 
# However, under Microsoft Windows you'll probably crash the Python interpreter if you try lists of more than about 2000 elements. 
# On a lab machine or on the quiz server, a list size of 10,000 will be fine, provided you've made the necessary change to the code so it's O(n) rather than O(n2).

# import sys
# sys.setrecursionlimit(100000)

# def dumbo_func(data, i=0):
#     """Takes a list of numbers and does weird stuff with it"""
#     if i >= len(data):
#         return 0
#     else:
#         if (data[i] // 100) % 3 != 0:
#             return 1 + dumbo_func(data, i+1)
#         else:
#             return dumbo_func(data, i+1)

####QUESTION 4

# Define a function my_enumerate(items) that behaves in a similar way to the built-in enumerate. 
# It should return a list of tuples (i, item) where item is the ith item, with a 0 origin, of the list items (see the examples below). 
# Check the test cases for how the function should work. 
# Your function must not call either of python's inbuilt enumerate or zip functions and cannot use any slices or loops nor import anything.

# Because slices are disallowed, you will need to pass in an extra parameter as explained in the above info panel.

# A O(n2) solution is acceptable here, though a O(n) solution is better (and perfectly possible).

# def my_enumerate(items, i=0):
#     if i >= len(items):
#         return []
#     return [(i, items[i])] + my_enumerate(items, i+1)

# ans = my_enumerate(['dog', 'pig', 'cow'])
# print(ans)

####QUESTION 5.a

# Herbert the Heffalump is trying to climb up a scree slope. 
# He finds that the best approach is to rush up the slope until he's exhausted, then pause to get his breath back. 
# However, while he pauses each time, the slope settles underneath him, carrying him back down part of the slope he just climbed.

# Write a function num_rushes(slope_height, rush_height_gain, back_sliding) that calculates 
# how many rushes it takes Herbert to climb up a slope of height slope_height metres, 
# given that each rush gains him rush_height_gain metres before he slides back back_sliding metres during the pause before the next rush. 
# The final rush will still be counted as 1 rush, even though it may be of shorter duration than the previous rushes.

# This implementation of num_rushes must be written without any loops and without any import statements.

# You can write this function efficiently with or without defining additional parameters.

# def num_rushes(slope_height, rush_height_gain, back_sliding, rushes=1):
#     distance_between = slope_height - rush_height_gain + back_sliding
#     if rush_height_gain >= slope_height:
#         return rushes
#     return num_rushes(distance_between, rush_height_gain, back_sliding, rushes+1)

# #     distance_between = (slope_height - rush_height_gain) + back_sliding
# #     return num_rushes(distance_between, rush_height_gain, back_sliding) + 1
# ans = num_rushes(100, 10, 0)
# print(ans)

####QUESTION 5.b
# Herbert tires rapidly as he attempts to climb the slope (Heffalumps are heavy), so each of his rushes gains him only 95% as much distance as his previous rush. 
# This means that if his first rush gains him rush_height_gain metres, then his second rush will only gain him 0.95 * rush_height_gain metres, 
# his third rush 0.95 * 0.95 * rush_height_gain metres, and so on. Fortunately, his back sliding reduces in the same way.

# Modify your previous function to account for the 5% reduction in height gain and back sliding on each rush. Usual rules about loops and pylint apply.

# You can write this function efficiently with or without defining additional parameters.

# def num_rushes(slope_height, rush_height_gain, back_sliding, rushes=1):
#     distance_between = slope_height - rush_height_gain + back_sliding
#     if rush_height_gain >= slope_height:
#         return rushes
#     return num_rushes(distance_between, rush_height_gain*0.95, back_sliding*0.95, rushes+1)

# ans = num_rushes(100, 15, 7)
# print(ans)