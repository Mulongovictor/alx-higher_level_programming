def print_matrix_integer(matrix=[[]]):
    height = len(matrix)
    for i in range(height):
       width = len(matrix[i])
      for j in range(width):
          print("{}".format(matrix[i][j]),end="")
            if (j != width - 1):
                print(end=" ")
            else: 
                print()
