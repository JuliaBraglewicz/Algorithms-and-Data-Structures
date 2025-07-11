#not finished yet

import matplotlib.pyplot as plt

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
    
def plot_graph(self, v_color, e_color):
      for idx, v in enumerate(self.vertex):
            y, x = v.key
            plt.scatter(x, y, c=v_color)
            for n_idx, _ in self.neighbours(idx):
                yn, xn = self.getVertex(n_idx).key
                plt.plot([x, xn], [y, yn], color=e_color)