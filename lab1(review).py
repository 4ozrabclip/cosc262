####QUESTION 1
# def concat_list(strings):
#     if len(strings) == 0:
#         return ""
#     return strings[0] + concat_list(strings[1:])

# ans = concat_list(['a', 'hot', 'day'])
# print(ans)

####QUESTION 2
# def product(data):
#     return 1 if len(data) == 0 else data[0] * product(data[1:])

# print(product([1, 13, 9, -11]))

####QUESTION 3
# def backwards(s):
#     return "" if len(s) == 0 else s[-1] + backwards(s[:-1])


# print(backwards("Hi there!"))