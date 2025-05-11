import polska

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
        return Matrix(new_matrix)
    
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
        id1 = self.get_vertex_id(vertex1)
        id2 = self.get_vertex_id(vertex2)
        self.matrix[id1][id2] = edge
        self.matrix[id2][id1] = edge
    
    def delete_vertex(self, vertex):
        id = self.get_vertex_id(vertex)
        del self.vertices_lst[id]
        new_matrix = []
        for i in range(len(self.vertices_lst) + 1):
            if i == id:
                continue
            new_matrix.append(self.matrix[i][:])
            del new_matrix[len(new_matrix) - 1][id]
        self.matrix = Matrix(new_matrix)
    
    def delete_edge(self, vertex1, vertex2):
        id1 = self.get_vertex_id(vertex1)
        id2 = self.get_vertex_id(vertex2)
        self.matrix[id1][id2] = self.val
        self.matrix[id2][id1] = self.val

    def neighbours(self, vertex_id):
        for id, edge in enumerate(self.matrix[vertex_id]):
            if edge != self.val:
                yield (id, edge)

    def vertices(self):
        for id in range(len(self.vertices_lst)):
            yield id

    def get_vertex(self, vertex_id):
        return self.vertices_lst[vertex_id]
    
    def get_vertex_id(self, vertex):
        try:
            return self.vertices_lst.index(vertex)
        except ValueError:
            raise Exception("Vertex ID not found!")
    
class GraphList:
    def __init__(self):
        self.list ={}
        
    def is_empty(self):
        return len(self.list) == 0
        
    def insert_vertex(self, vertex):
        if vertex in self.list:
            return
        else:
            self.list[vertex] = {}
    
    def insert_edge(self, vertex1, vertex2, edge = None):
        if vertex1 not in self.list or vertex2 not in self.list:
            raise Exception("Vertex not found!")
        self.list[vertex1][vertex2] = edge
        self.list[vertex2][vertex1] = edge
    
    def delete_vertex(self, vertex):
        if vertex in self.list:
            for i in list(self.list.keys()):
                if vertex in self.list[i]:
                    del self.list[i][vertex]
            del self.list[vertex]
    
    def delete_edge(self, vertex1, vertex2):
        if vertex1 in self.list and vertex2 in self.list:
            if vertex2 in self.list[vertex1]:
                del self.list[vertex1][vertex2]
            if vertex1 in self.list[vertex2]:
                del self.list[vertex2][vertex1]

    def neighbours(self, vertex_id):
        if vertex_id in self.list:
            return self.list[vertex_id].items()

    def vertices(self):
        return self.list.keys()
    
    def get_vertex(self, vertex_id):
        return vertex_id

def main():
    matrix_graph = GraphMatrix()
    list_graph = GraphList()
    vertices = {}
    
    for rej in polska.slownik.keys():
        vertex = Vertex(rej)
        matrix_graph.insert_vertex(vertex)
        list_graph.insert_vertex(vertex)
        vertices[rej] = vertex
    
    for i, j in polska.graf:
        matrix_graph.insert_edge(vertices[i], vertices[j])
        list_graph.insert_edge(vertices[i], vertices[j])

    matrix_graph.delete_vertex(vertices['K'])
    matrix_graph.delete_edge(vertices['W'], vertices['L'])
    polska.draw_map(matrix_graph)

    list_graph.delete_vertex(vertices['K'])
    list_graph.delete_edge(vertices['W'], vertices['L'])
    polska.draw_map(list_graph)

if __name__ == "__main__":
    main()