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
        return new_matrix
    
    def __getitem__(self, index):
        return self.__matrix[index]
        
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
        
def main():
    m1 = Matrix([[1, 0, 2],[-1, 3, 1]])
    m2 = Matrix((2, 3), val = 1)
    m3 = Matrix([[3, 1], [2, 1], [1, 0]])
    print(transpose(m1))
    print(m1 + m2)
    print(m1 * m3)

if __name__ == "__main__":
    main()