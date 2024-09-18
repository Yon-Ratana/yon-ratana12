



# Ex2:
def uppercase(list):
    result = []
    for fruit in list:
        str = ''.join(fruit).lower()
        result.append(str)
    return result
list2D = [
    ['B', 'A', 'N', 'A', 'N', 'A'],
    ['C', 'O', 'C', 'O', 'N', 'U', 'T']
]
print(uppercase(list2D))

  

























# def find_duplicates(array):
#     duplicates = []
#     seen = set()
#     for num in array:
#         if num in seen:
#             if num not in duplicates:
#                 duplicates.append(num)
#         else:
#             seen.add(num)
#     return duplicates
# array1 = [9, 9, 8, 8, 8, 1, 3]
# print(find_duplicates(array1))  







