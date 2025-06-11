from copy import deepcopy

class Vertex:
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.key == other.key
        return False
        
    def __hash__(self):
        return hash(self.key)
        
    def __repr__(self):
        return self.key
        
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
    
    def transpose(self):
        transpose_matrix = Matrix((self.size()[1], self.size()[0]))
        for i in range(self.size()[0]):
            for j in range(self.size()[1]):
                transpose_matrix[j][i] = self.__matrix[i][j]
        return transpose_matrix
    
    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.__matrix == other.__matrix
        else:
            return False
        
    def copy(self):
        return Matrix(deepcopy(self.__matrix))
    
class GraphMatrix:
    def __init__(self, val = 0):
        self.matrix = Matrix((0, 0), val)
        self.vertices_lst = []
        self.val = val
        
    def is_empty(self):
        return len(self.vertices_lst) == 0
        
    def insert_vertex(self, vertex):
        if vertex in self.vertices_lst:
            return
        else:
            new_matrix = []
            for i in range(len(self.vertices_lst)):
                new_matrix.append(self.matrix[i] + [self.val])
            new_matrix.append([self.val] * (len(self.vertices_lst) + 1))
            self.vertices_lst.append(vertex)
            self.matrix = Matrix(new_matrix)

    def insert_edge(self, vertex1, vertex2, edge = 1):
        id1 = self.vertices_lst.index(vertex1)
        id2 = self.vertices_lst.index(vertex2)
        self.matrix[id1][id2] = edge
        # self.matrix[id2][id1] = edge
    
    def delete_vertex(self, vertex):
        id = self.vertices_lst.index(vertex)
        del self.vertices_lst[id]
        new_matrix = []
        for i in range(len(self.vertices_lst) + 1):
            if i == id:
                continue
            new_matrix.append(self.matrix[i][:])
            del new_matrix[len(new_matrix) - 1][id]
        self.matrix = Matrix(new_matrix)
    
    def delete_edge(self, vertex1, vertex2):
        id1 = self.vertices_lst.index(vertex1)
        id2 = self.vertices_lst.index(vertex2)
        self.matrix[id1][id2] = self.val
        # self.matrix[id2][id1] = self.val

    def neighbours(self, vertex_id):
        for id, edge in enumerate(self.matrix[vertex_id]):
            if edge != self.val:
                yield (id, edge)

    def vertices(self):
        for id in range(len(self.vertices_lst)):
            yield id

    def get_vertex(self, vertex_id):
        return self.vertices_lst[vertex_id]
    
def ullman(used_cols, current_row, M, G, P, correct, count = 0):
    count += 1
    if current_row == M.size()[0]:
        result = M * (M * G.matrix).transpose()
        if result == P.matrix:
            correct.append(M.copy())
        return count
    for c in range(M.size()[1]):
        if not used_cols[c]:
            used_cols[c] = True
            for i in range(M.size()[1]):
                if i != c:
                    M[current_row][i] = 0
                else:
                    M[current_row][i] = 1
            count = ullman(used_cols, current_row + 1, M, G, P, correct, count)
            used_cols[c] = False
    return count

def ullman_2(used_cols, current_row, M, G, P, correct, count = 0):
    count += 1
    if current_row == M.size()[0]:
        result = M * (M * G.matrix).transpose()
        if result == P.matrix:
            correct.append(M)
        return count
    M_copy = M.copy()
    for c in range(M_copy.size()[1]):
        if not used_cols[c] and M[current_row][c] != 0:
            used_cols[c] = True
            for i in range(M_copy.size()[1]):
                if i != c:
                    M_copy[current_row][i] = 0
                else:
                    M_copy[current_row][i] = 1
            count = ullman_2(used_cols, current_row + 1, M_copy, G, P, correct, count)
            used_cols[c] = False
    return count

def prune(M, G, P):
    changed = True
    while changed:
        changed = False
        for i in range(M.size()[0]):
            for j in range(M.size()[1]):
                if M[i][j] == 1:
                    for x, _ in P.neighbours(i):
                        match = False
                        for y, _ in G.neighbours(j):
                            if M[x][y] == 1:
                                match = True
                                break
                        if not match:
                            M[i][j] = 0
                            changed = True
                            break

def ullman_3(used_cols, current_row, M, G, P, correct, count = 0):
    count += 1
    if current_row == M.size()[0]:
        result = M * (M * G.matrix).transpose()
        if result == P.matrix:
            correct.append(M)
        return count
    M_copy = M.copy()
    prune(M_copy, G, P)
    for c in range(M_copy.size()[1]):
        if not used_cols[c] and M[current_row][c] != 0:
            used_cols[c] = True
            for i in range(M_copy.size()[1]):
                if i != c:
                    M_copy[current_row][i] = 0
                else:
                    M_copy[current_row][i] = 1
            count = ullman_3(used_cols, current_row + 1, M_copy, G, P, correct, count)
            used_cols[c] = False
    return count
    
def main():
    graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)]
    graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)]

    G = GraphMatrix()

    for v1, v2, e in graph_G:
        vertex1 = Vertex(v1)
        vertex2 = Vertex(v2)
        G.insert_vertex(vertex1)
        G.insert_vertex(vertex2)
        G.insert_edge(vertex1, vertex2)
        G.insert_edge(vertex2, vertex1)

    P = GraphMatrix()

    for v1, v2, e in graph_P:
        vertex1 = Vertex(v1)
        vertex2 = Vertex(v2)
        P.insert_vertex(vertex1)
        P.insert_vertex(vertex2)
        P.insert_edge(vertex1, vertex2)
        P.insert_edge(vertex2, vertex1)

    M = Matrix((len(P.vertices_lst), len(G.vertices_lst)))

    correct_1 = []
    count = ullman([False] * 6, 0, M, G, P, correct_1)
    print(len(correct_1), count)

    M0 = Matrix((len(P.vertices_lst), len(G.vertices_lst)))
    for i in range(len(P.vertices_lst)):
        deg_p = sum(P.matrix[i])
        for j in range(len(G.vertices_lst)):
            deg_g = sum(G.matrix[j])
            if deg_p <= deg_g:
                M0[i][j] = 1

    correct_2 = []
    count = ullman_2([False] * 6, 0, M0, G, P, correct_2)
    print(len(correct_2), count)

    correct_3 = []
    count = ullman_3([False] * 6, 0, M0, G, P, correct_3)
    print(len(correct_3), count)

if __name__ == "__main__":
    main()