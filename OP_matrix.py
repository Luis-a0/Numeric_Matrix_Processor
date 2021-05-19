def int_or_float(x):
    if "." in x:
        return float(x)
    else:
        return int(x)

def make_matrix_input(row_x):
    matrix = [list(map(int_or_float, input().split(" "))) for _ in range(int(row_x))]
    return matrix

def sum_matrix(x, y):
    c = [[] for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(x[0])):
            c[i].append(x[i][j] + y[i][j])
    return c
    
def print_matrix(matrix):
    for fila in matrix:
        print(' '.join(str(element) for element in fila))

def scalar_mult_matrix(matrix, scalar):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] *= scalar
    return matrix
    
def sum_two_matrices():
    row_x, col_x = input("Enter size of first matrix: ").split(" ")
    print("Enter first matrix: ")
    matrix_x = make_matrix_input(row_x)

    row_y, col_y = input("Enter size of second matrix: ").split(" ")
    print("Enter second matrix: ")
    matrix_y = make_matrix_input(row_y)
    
    if (row_x != row_y) or (col_x != col_y):
        print("ERROR")
    else:
        print("The result is: ")
        print_matrix(sum_matrix(matrix_x, matrix_y))
    
def mul_scalar():
    row_x, col_x = input("Enter size of matrix: ").split(" ")
    print("Enter matrix: ")
    A = make_matrix_input(row_x)
    scalar = int_or_float(input("Enter constant: "))
    B = scalar_mult_matrix(A, scalar)
    print(print("The result is: "))
    print_matrix(B)
    
def mul_two_matrices():
    row_x, col_x = input("Enter size of first matrix: ").split(" ")
    print("Enter first matrix: ")
    matrix_x = make_matrix_input(row_x)

    row_y, col_y = input("Enter size of second matrix: ").split(" ")
    print("Enter second matrix: ")
    matrix_y = make_matrix_input(row_y)
    
    if (row_x != col_y):
        print("ERROR")
    else:
        print("The result is: ")
        print_matrix(mul_matrix(matrix_x, matrix_y))

def menu():
    entrada = None

    while entrada != 0:
        entrada = int(input("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
0. Exit
Your choice: """))
        if entrada == 1:
            sum_two_matrices()
            print("")
        elif entrada == 2:
            mul_scalar()
        elif entrada == 3:
            mult_matrix()
            
if __name__ == "__main__":
    menu()
