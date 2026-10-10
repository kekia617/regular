import numpy as np




def matrix_gen(m, n):
    print("Start a matrix:")
    matrix = []

    for i in range(m*n):
        matrix.append(int(input("come, give a num: ")))

    j = 0

    A = np.array(matrix[j:j+n])

    for i in range(m-1):
        j += n
        A = np.vstack((A, matrix[j: j + n]))
        

    return A

if __name__ == '__main__':
    m = int(input("What's the row number? "))
    n = int(input("What's the column nember? "))
    matrix_gen(m, n)