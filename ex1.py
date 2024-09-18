#Q1
def uppercase(array2D):
    sum = ["Column Error"]
    for i in array2D:
        for j in array2D:
            array2D[2] = "*"
            sum = array2D
    return sum
array2D = [["A", "B", "C"],["D", "F", "C"],["A", "A", "F"]]       
print( uppercase(array2D))