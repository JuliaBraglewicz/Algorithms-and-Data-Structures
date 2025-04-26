class Matrix:
    def __init__(self, __matrix, val = 0):
        if isinstance(__matrix, tuple):
            self.__matrix = [[val for _ in range(__matrix[1])] for _ in range(__matrix[0])]
        else:
            self.__matrix = __matrix
    
    def __add__(self, other):
        if self.size() != other.size():
            raise Exception("Wrong size!")
        new_matrix = []
        for i in range(self.size()[0]):
            new_matrix.append([self[i][j] + other[i][j] for j in range(self.size()[1])])
        return Matrix(new_matrix)
    
    def __mul__(self, other):
        if self.size()[1] != other.size()[0]:
            raise Exception("Wrong size!")
        new_matrix = Matrix((self.size()[0], other.size()[1]))
        for i in range(self.size()[0]):
            for j in range(other.size()[1]):
                for k in range(other.size()[0]):
                    new_matrix[i][j] += self[i][k] * other[k][j]
        return Matrix(new_matrix)
    
    def __getitem__(self, index):
        return self.__matrix[index]
        
    def __setitem__(self, index, val):
        self.__matrix[index] = val
        
    def __str__(self):
        text = ''
        for row in self.__matrix:
            text += '| '
            for col in row:
                text += str(col) + ' '
            text += '|\n'
        return text
        
    def size(self):
        return len(self.__matrix), len(self.__matrix[0])
        
def transpose(matrix):
    transpose_matrix = Matrix((matrix.size()[1], matrix.size()[0]))
    for i in range(matrix.size()[0]):
        for j in range(matrix.size()[1]):
            transpose_matrix[j][i] = matrix[i][j]
    return transpose_matrix
    
def d_2x2(matrix):
    if matrix.size()[0] == 2 and matrix.size()[1] == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    else:
        raise Exception("Wrong size!")
        
def chio(matrix):
    if matrix.size()[0] == 2 and matrix.size()[1] == 2:
        return d_2x2(matrix)
    sign = 1
    if matrix[0][0] == 0:
        for i in range(matrix.size()[0]):
            if matrix[i][0] != 0:
                matrix[0], matrix[i] = matrix[i], matrix[0]
                sign *= -1
                break
    if matrix.size()[0] == matrix.size()[1] and matrix.size()[0] > 2:
        new_matrix = []
        for i in range(matrix.size()[0] - 1):
            new_row = []
            for j in range (matrix.size()[1] - 1):
                new_row.append(d_2x2(Matrix([[matrix[0][0], matrix[0][j+1]], [matrix[i+1][0], matrix[i+1][j+1]]])))
            new_matrix.append(new_row)
    return (sign/(matrix[0][0] ** (matrix.size()[0] - 2))) * chio(Matrix(new_matrix))
        
def main():
    m4 = Matrix([[5, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
    print(chio(m4))
    m5 = Matrix([[0, 1, 1, 2, 3], [4, 2, 1, 7, 3], [2, 1, 2, 4, 7], [9, 1, 0, 7, 0], [1, 4, 7, 2, 2]])
    print(chio(m5))
    
if __name__ == "__main__":
    main()