
def checkRoomAvailable(array2D, row, column):
    roomFree = False
    for i in range(len(array2D)) :
        for j in range(len(array2D[i])):
            if i == row and j == column and array2D[i][j] != 1:
                roomFree = True
    return roomFree

def countRoomLive(array2D):
    countRoom = 0
    for i in range(len(array2D)) :
        for j in range(len(array2D[i])):
            if array2D[i][j] == 1:
                countRoom += 1
    return countRoom
array2D = [
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 1]
          ]
row = 0
column = 0
message = "CANNOT ADD"
if checkRoomAvailable(array2D, row, column) and countRoomLive(array2D) < 3:
    message = "CAN ADD"
print(message)


