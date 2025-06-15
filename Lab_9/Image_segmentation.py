import graf_mst
import cv2
import numpy as np

class Vertex:
    def __init__(self, key, color = None):
        self.key = key
        self.color = color

    def __eq__(self, other):
        if isinstance(other, Vertex):
            return self.key == other.key
        return False
        
    def __hash__(self):
        return hash(self.key)
        
    def __repr__(self):
        return self.key
    
    def set_color(self, color):
        self.color = color
        
    def get_color(self):
        return self.color
    
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
    
    def set_color(self, vertex, color):
        vertex.color = color

    def get_color(self, vertex):
        return vertex.color
        
def Prim_MST(graph):
    intree = {v: 0 for v in graph.vertices()}
    distance = {v: float('inf') for v in graph.vertices()}
    parent = {v: None for v in graph.vertices()}

    MST = GraphList()

    start = graph.get_vertex(next(iter(graph.vertices())))
    MST.insert_vertex(start)
    v = start
    length = 0

    while intree[v] == 0:
        intree[v] = 1

        for n, e in graph.neighbours(v):
            if intree[n] == 0 and e < distance[n]:
                distance[n] = e
                parent[n] = v

        min = float('inf')

        for vertex in graph.vertices():
            if intree[vertex] == 0 and distance[vertex] < min:
                min = distance[vertex]
                v = vertex

        MST.insert_vertex(v)

        if intree[v] == 0 and parent[v] is not None:
            MST.insert_edge(v, parent[v], distance[v])
            MST.insert_edge(parent[v], v, distance[v])
            length += distance[v]

    return MST, length

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
    
def traverse(graph, start, color):
    segment = {}
    stack = [start]
    visited = set()
    while stack:
        vertex_id = stack.pop()
        if vertex_id not in visited:
            vertex_id.set_color(color)
            segment[vertex_id] = color
            visited.add(vertex_id)
            for n, _ in reversed(list(graph.neighbours(vertex_id))):
                if n not in visited:
                    stack.append(n)
    return segment

    
def main():
    graph = GraphList()
    I = cv2.imread('sample.png',cv2.IMREAD_GRAYSCALE)
    
    YY, XX = I.shape
    for j in range(YY):
        for i in range(XX):
            v = Vertex(str(XX * j + i))
            v.set_color(I[j][i])
            graph.insert_vertex(v)
            
    for j in range(1, YY - 1):
        for i in range(1, XX - 1):
            graph.insert_edge(Vertex(str(XX * j + i)), Vertex(str(XX * (j - 1) + (i - 1))), abs(I[j][i].astype(int) - I[j - 1][i - 1].astype(int)))
            graph.insert_edge(Vertex(str(XX * j + i)), Vertex(str(XX * (j + 1) + (i + 1))), abs(I[j][i].astype(int) - I[j + 1][i + 1].astype(int)))
            graph.insert_edge(Vertex(str(XX * j + i)), Vertex(str(XX * (j - 1) + (i + 1))), abs(I[j][i].astype(int) - I[j - 1][i + 1].astype(int)))
            graph.insert_edge(Vertex(str(XX * j + i)), Vertex(str(XX * (j + 1) + (i - 1))), abs(I[j][i].astype(int) - I[j + 1][i - 1].astype(int)))
            graph.insert_edge(Vertex(str(XX * j + i)), Vertex(str(XX * (j - 1) + i)), abs(I[j][i].astype(int) - I[j - 1][i].astype(int)))
            graph.insert_edge(Vertex(str(XX * j + i)), Vertex(str(XX * (j + 1) + i)), abs(I[j][i].astype(int) - I[j + 1][i].astype(int)))
            graph.insert_edge(Vertex(str(XX * j + i)), Vertex(str(XX * j + (i - 1))), abs(I[j][i].astype(int) - I[j][i - 1].astype(int)))
            graph.insert_edge(Vertex(str(XX * j + i)), Vertex(str(XX * j + (i + 1))), abs(I[j][i].astype(int) - I[j][i + 1].astype(int)))
    
    MST, length = Prim_MST(graph)

    max_edge = None
    max_weight = -1

    for v in MST.vertices():
        for u, w in MST.neighbours(v):
            if w > max_weight:
                max_weight = w
                max_edge = (v, u)

    if max_edge:
        v1, v2 = max_edge
        MST.delete_edge(v1, v2)
    
    IS = np.zeros((YY,XX),dtype='uint8')
    
    segment1 = traverse(MST, v1, 100)
    segment2 = traverse(MST, v2, 200)
    
    for vertex, color in segment1.items():
        key = vertex.key
        y = int(key) // XX
        x = int(key) % XX
        IS[y, x] = color
        
    for vertex, color in segment2.items():
        key = vertex.key
        y = int(key) // XX
        x = int(key) % XX
        IS[y, x] = color
        
    cv2.imshow("Wynik", IS)
    cv2.waitKey()
    
if __name__ == "__main__":
    main()