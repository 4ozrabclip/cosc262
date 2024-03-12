# strings = ['a','good','dog','ok']
# def main(strings):
#     if len(strings) == 0:
#         return ''
#     else:
#         return strings[0] + str(main(strings[1:]))
    
# here = main(strings)

# print(here)

# QUESTION 2
# data = [1, 13, 9, -11]
# def product(data):
#     if len(data) == 0:
#         return 1
#     else:
#         return data[0] * product(data[1:])
    
# here = product(data)

# print(here)

#QUESTION 3
# s = "Hi there!"
# def backwards(s):
#     if len(s) == 0:
#         return ""
#     return backwards(s[1:]) + s[0]

# here = backwards(s)

# print(here)

#QUESTION 4
# data = [0, 1, 12, 13, 14, 9, -11, -20]
# def odds(data):
#     if len(data) == 0:
#         return 1
#     else:
#         if odds(data[0] % 2) == 0:
#             pass
            
# here = odds(data)
# print(here)

# numbers = [8, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# def almost_all(numbers):
#     summed = sum(numbers)
#     return [summed - x for x in numbers]

# here = almost_all(numbers)
# print(here)

numbers = [8, 2, 5, 4, 5, 6, 7, 8, 9]
def foo(numbers): 
    result = [] 
    for i in range(len(numbers)): 
        sub = sorted(numbers[i:])
        result.append(sub[0])
    return result


here = foo(numbers)
print(here)



