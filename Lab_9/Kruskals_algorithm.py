import graf_mst

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
    
    def get_edges(self):
        edges = []
        for vertex1 in self.vertices():
            for vertex2, edge in self.neighbours(vertex1):
                edges.append((repr(self.get_vertex(vertex1)), repr(self.get_vertex(vertex2)), edge))
        return edges
    
    def get_num_vertex(self):
        return len(self.list)

class UnionFind:
    def __init__(self, n):
        self.p = list(range(1, n + 1))
        self.size = [1] * n
        self.n = n

    def find(self, v):
        root = self.p[v - 1]
        if root != v:
            root = self.find(root)
        return root
    
    def union_sets(self, s1, s2):
        root1 = self.find(s1)
        root2 = self.find(s2)
        if root1 == root2:
            return None
        else:
            size1 = self.size[root1 - 1]
            size2 = self.size[root2 - 1]
            if size1 >= size2:
                self.p[root2 - 1] = root1
                self.size[root1 - 1] += self.size[root2 - 1]
            else:
                self.p[root1 - 1] = root2
                self.size[root2 - 1] += self.size[root1 - 1]

    def same_component(self, s1, s2):
        return self.find(s1) == self.find(s2)
    
def Kruskal_MST(graph):
    edge_lst = sorted(graph.get_edges(), key = lambda x: x[2])
    uf = UnionFind(graph.get_num_vertex())
    mst_edges = []
    length = 0

    for v1, v2, e in edge_lst:
        if not uf.same_component(ord(v1) - 64, ord(v2) - 64):
            uf.union_sets(ord(v1) - 64, ord(v2) - 64)
            mst_edges.append((v1, v2, e))
            length += e

    MST = GraphList()

    for v1, v2, edge in mst_edges:
        vertex1 = Vertex(v1)
        vertex2 = Vertex(v2)
        MST.insert_vertex(vertex1)
        MST.insert_vertex(vertex2)
        MST.insert_edge(vertex1, vertex2, edge)

    return MST, length

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
        
def main():
    find_union =UnionFind(5)
    find_union.union_sets(1, 2)
    find_union.union_sets(4, 5)
    print(find_union.same_component(1, 2))
    print(find_union.same_component(2, 3))
    print(find_union.same_component(4, 5))
    find_union.union_sets(3, 1)
    print(find_union.same_component(1, 2))
    print(find_union.same_component(2, 3))
    print(find_union.same_component(4, 5))

    graph = GraphList()

    for v1, v2, edge in graf_mst.graf:
        vertex1 = Vertex(v1)
        vertex2 = Vertex(v2)
        graph.insert_vertex(vertex1)
        graph.insert_vertex(vertex2)
        graph.insert_edge(vertex1, vertex2, edge)

    MST, length = Kruskal_MST(graph)

    printGraph(MST)

if __name__ == "__main__":
    main()