import numpy as np

vierkant = np.array([5, 0, 0,
                   0, 0, 4,
                   0, 0, 6])

x1 = vierkant[0]
x2 = vierkant[1]
x3 = vierkant[2]
x4 = vierkant[3]
x5 = vierkant[4]
x6 = vierkant[5]
x7 = vierkant[6]
x8 = vierkant[7]
x9 = vierkant[8]
t = -1

regels = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
laatste_regel = [3*4]

Matrix = []
for x in regels:
    rij = []
    result = 0
    for count in range(9):
        if count in x:
            if vierkant[count] != 0:
                rij.append(0)
            else:
                rij.append(1)
        else:
            rij.append(0)
    rij.append(t)
    Matrix.append(rij)

print(Matrix)

vector_b = []
for x in regels:
    waarde = []
    for getal in x:
        waarde.append(vierkant[getal])
    vector_b.append(-1*sum(waarde))
print(vector_b)

# print(np.shape(Matrix)[0])
# # adding the last row manual
# last_row = [0 for x in range(len(vierkant))]
# last_row.append(-1)
# if vierkant[4] !=0:
#     last_row[4] = 0
#     vector_b.append(0 - (3 * vierkant[4]))
# else:
#     last_row[4] = 3
#     vector_b.append(0)
# Matrix.append(last_row)

# convert the lists into numpy arrays for processing
matrix_A = np.array(Matrix)
# vector_b = np.transpose(np.array([vector_b]))
vector_b = np.array(vector_b)

# print the lists
print("Matrix A:")
print(matrix_A)
print("\nDe vector b van de resultaat:")
print(vector_b)


def delete_column(chosen_matrix):
    """Checks for an empty column and deletes one"""

    chosen_matrix = list(chosen_matrix)
    col_number = 0

    #
    for col in range(0, len(chosen_matrix[0])):
        is_zero_column = True
        for row in range(0, len(chosen_matrix)):
            if chosen_matrix[row][col_number] != 0:
                is_zero_column = False
                break
        # the column is a zero-column
        if is_zero_column:
            chosen_matrix = np.array(chosen_matrix)
            chosen_col = [x for x in range(0, len(chosen_matrix) + 1) if x != col_number]
            return chosen_matrix[:, chosen_col], col_number

        # search the next column
        col_number += 1


# printing the shape of the matrix
print("Shape of the matrix before erase:\n{0}\n".format(np.shape(matrix_A)))

# erase a column and return the new values into their respective variables
changed_matrix = delete_column(matrix_A)
matrix_B = changed_matrix[0]
deleted_col = changed_matrix[1]
print("Shape of matrix after erase:\n{0}".format(np.shape(matrix_B)))
# calculate the pseudo-inverse of the matrix
pseudo_inverse = np.linalg.pinv(matrix_B)

# take the dot product of the pseudo inverse and the result vector
solve_vector = np.dot(pseudo_inverse, vector_b)
solve_vector = list(solve_vector)

# add the deleted column back
solve_vector.insert(deleted_col, 0)

# round all the numbers to .1 accuracy
for x in range(0, len(solve_vector)):
    solve_vector[x] = round(solve_vector[x], 2)

# save the total sum number
total_number = solve_vector.pop()

# reshape the vector as a n x n matrix
solve_vector = np.reshape(solve_vector, (3, 3))

check_square = list([[5, 0, 0,],[0, 0, 4],[0, 0, 6]])
solved_square = []
for row in range(0, len(check_square)):
    for num in range(0, len(check_square[0])):
        if check_square[row][num] > 0:
            solved_square.append(check_square[row][num])
        else:
            solved_square.append(solve_vector[row][num])

# reshape the square and print all the info
solved_square = np.reshape(solved_square, (3, 3))
print("The solved square:\n{0}\n".format(solved_square))
print("The side sum is: {0}".format(total_number))
