# QUESTION 1

# Recursion, Divide and Conquer

# Take any natural number n. If n is even, divide it by 2 to get n//2. If n is odd, multiply it by 3 and add 1 to obtain 3n+1. 
# The Collatz conjecture claims that no matter what number you start with, you will always eventually reach 1. For example for n=22

# , the following sequence of numbers will be generated:

# 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1

# The Collatz conjecture has been tested on all values up to 1018
# and it holds. No one has managed to prove the Collatz conjecture. That is why it is still called a conjecture and not a theorem.

# For a positive n, the Collatz sequence-length of n is the number of numbers generated in the Collatz sequence starting from n up to 1 (including n and 1). 
# In the example above, the sequence length of 22 is 16.

# Write a recursive function sequence_length(n) to compute the Collatz sequence length of a the given positive integer. 
# You are not allowed to import any module or use any types of loop (for, while, list comprehension, ...).

# n = 22
# def sequence_length(n):
#     count = 0
#     if n == 1:
#         return 1
#     elif n % 2 == 0:
#         count += sequence_length(n//2) + 1
#     else:
#         count += sequence_length((n*3) + 1) + 1

#     return count

# here = sequence_length(n)
# print(here)
########################################################################

# QUESTION 2

# Write a recursive function recursive_divide(x, y) to perform integer division without any of the following:

#     importing a module
#     using operators *, /, //, or %
#     using any types of loop (for, while, list comprehension, ...)

# The function must return what x//y would return in Python 3. Assume x >= 0 and y > 0 is true.

# def recursive_divide(x, y):
#     result = 1
#     if x > y:
#         result += recursive_divide(x-y, y)
#     return result

# def recursive_divide(x, y):  ######## SOLUTION
#     if x < y:
#         return 0
#     return 1 + recursive_divide(x-y, y)

# # # while y is over 0 we will get x and minus 1 

# here = recursive_divide(8, 3)
# # 1 + 2

# print(here)

############################################################################

################## QUESTION 3 #########################

# import sys
# sys.setrecursionlimit(100000)
# data = [677, 90, 785, 875, 7, 90393, 10707]
# def dumbo_func(data, start_index=0):
#     """Takes a list of numbers and does weird stuff with it"""
#     if len(data) <= start_index:
#         return 0
#     else:
#         if (data[start_index] // 100) % 3 != 0:
#             return 1 + dumbo_func(data, start_index + 1)
#         else:
#             return dumbo_func(data, start_index + 1)
        
# yeah = dumbo_func(data)

# print(yeah)

###################### QUESTION 4 ##########################

# def my_enumerate(items, i=0):
#     if len(items) <= i:
#         return []
#     else:
#         tup = (i, items[i])
#         return [tup] + my_enumerate(items, i+1)


# here = my_enumerate([10, 20, 30])

# print(here)
        
################################## QUESTION 5.a ##################################
        
# def num_rushes(slope_height, rush_height_gain, back_sliding):

#     if rush_height_gain >= slope_height:
#         return 1
#     distance_between = (slope_height - rush_height_gain) + back_sliding
#     return num_rushes(distance_between, rush_height_gain, back_sliding) + 1

# here = num_rushes(100, 10, 0)

# print(here)

################################### QUESTION 5.b ####################################

# def num_rushes(slope_height, rush_height_gain, back_sliding):
#     if rush_height_genting adjacency lists, in order to be able to use the samain >= slope_height:
#         return 1
#     distance_between = slope_height - rush_height_gain + back_sliding
#     return 1 + num_rushes(distance_between, rush_height_gain*0.95, back_sliding*0.95)

# here = num_rushes(10, 10, 9)

# print(here)


###################################### QUESTION 12 ######################################

# NUM_RMDS = 9   # number of right-most digits required

# def multiply2by2(A, B):

#     product = [
#         [A[0][0]*B[0][0]+A[0][1]*B[1][0],	A[0][0]*B[0][1]+A[0][1]*B[1][1]],	 
#         [A[1][0]*B[0][0]+A[1][1]*B[1][0],	A[1][0]*B[0][1]+A[1][1]*B[1][1]]
#         ]
    

#     product = [[x % 10**NUM_RMDS for x in row] for row in product]
    
#     return product

# def matrix_power(A, n):

#     if n == 0:
#         return [[1, 0],
#                 [0, 1]]
#     elif n == 1:
#         return A

#     p = matrix_power(A, n//2)
#     if n % 2 == 0:
#         return multiply2by2(p, p)
#     else:
#         return multiply2by2(A, multiply2by2(p, p))
    

# def fib(n):
    
#     A = [[1, 1], 
#          [1, 0]]
         
#     return matrix_power(A, n)[0][1]

# print(fib(100))

# # def power(a, n):
# #     if n == 0:
# #         return 1
# #     else:
# #         p = power(a, n//2)
# #         if n % 2 == 0:
# #             return p * p 
# #         return a * p * p
    
# # print(power(2, 5))

def all_pairs(list1, list2):
    tuples = []
    # if len(list1) == 0 and len(list2) == 0:
    #     return []
    
    tuples.append(all_pairs(all_pairs(list1, list2), all_pairs(list1, list2)))

    return tuples



print(all_pairs([1, 2], [10, 20, 30]))