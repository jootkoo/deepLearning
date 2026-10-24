matrix = [[10,20,30],
          [40,50,60],
          [70,80,90]]
print(matrix[1][1])
print(matrix[2])
matrix[0][2] = 35
print(matrix)

for i in range(len(matrix)):
    print(matrix[i])