def number(num1,num2):
    result = (num1,num2)
    message = ""
    for num in result:
        if num1 != num2:
            message = "not equal"
        elif num1 == num2:
            message = "equal"
    return message
array1 = [[0,0,7],[0,0,7]]
array2 = [[1,0,7],[0,3,7]]
print(number(array1,array2))

