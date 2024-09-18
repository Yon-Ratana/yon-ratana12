
# Ex3 :
def countNumber(array, number):
    count=0
    for num in array:
        if num ==number:
            count +=1
    return count
def alreadyExist(array,number):
    alreadyExist = False
    for num in array:
        if number == num:
            alreadyExist = True
    return alreadyExist
array = [9,9,8,8,8,1,3,3]
new_array =[]
for num in array:
    if countNumber(array,num) > 1 and not alreadyExist(new_array, num):
        new_array.append(num)
print(new_array)


# Ex3 :
# def countNumber(array, number):
#     count=0
#     for num in array:
#         if num ==number:
#             count +=1
#     return count

# def alreadyExist(array,number):
#     alreadyExist = False
#     for num in array:
#         if number == num:
#             alreadyExist = True
#     return alreadyExist

# def findNumberMoreThanOne(array):
#     new_array =[]
#     for num in array:
#         if countNumber(array,num) > 1 and not alreadyExist(new_array, num):
#             new_array.append(num)
#     return new_array

# array2D= [[9,9,8,8,8,1,3,3],[1,1,3]]
# for i in range(len(array2D)):
#     array2D[i] = findNumberMoreThanOne(array2D[i])
# print(array2D)