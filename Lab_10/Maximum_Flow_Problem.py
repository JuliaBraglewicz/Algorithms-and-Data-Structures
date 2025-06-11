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
    
class Edge:
    def __init__(self, capacity, is_residual):
        self.is_residual = is_residual
        if isinstance(self.is_residual, bool) and not self.is_residual:
            self.capacity = capacity
            self.flow = 0
            self.residual_capacity = capacity
        elif isinstance(self.is_residual, bool) and self.is_residual:
            self.capacity = 0
            self.flow = 0
            self.residual_capacity = 0
        else:
            raise Exception("Wrong edge type!")
        
    def __repr__(self):
        return f"{self.capacity} {self.flow} {self.residual_capacity} {self.is_residual}"

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
        # self.list[vertex2][vertex1] = edge
    
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
            # if vertex1 in self.list[vertex2]:
            #     del self.list[vertex2][vertex1]

    def neighbours(self, vertex_id):
        if vertex_id in self.list:
            return self.list[vertex_id].items()

    def vertices(self):
        return self.list.keys()
    
    def get_vertex(self, vertex_id):
        return vertex_id
    
    def get_edge(self, vertex1_id, vertex2_id):
        return self.list[self.get_vertex(vertex1_id)][self.get_vertex(vertex2_id)]
    
def BFS(graph, start):
    visited = set()
    parent = {}
    queue = [start]
    visited.add(start)
    while queue:
        vertex_id = queue.pop(0)
        for n, e in graph.neighbours(vertex_id):
            if n not in visited and e.residual_capacity > 0:
                queue.append(n)
                visited.add(n)
                parent[n] = vertex_id
    return parent
                
def min_capacity(graph, start, end, parent):
    current = end
    if current not in parent:
        return 0
    else:
        min_residual_capacity = float('inf')
        while current != start:
            residual_capacity = graph.get_edge(parent[current], current).residual_capacity
            if residual_capacity < min_residual_capacity:
                min_residual_capacity = residual_capacity
            current = parent[current]
        return min_residual_capacity
    
def path_augmentation(graph, start, end, parent, min_capacity):
    current = end
    while current != start:
        edge = graph.get_edge(parent[current], current)
        reverse = graph.get_edge(current, parent[current])
        edge.residual_capacity -= min_capacity
        reverse.residual_capacity += min_capacity
        if not edge.is_residual:
            edge.flow += min_capacity
        else:
            reverse.flow -= min_capacity
        current = parent[current]

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")
    
def main():
    graf_0 = [ ('s','u',2), ('u','t',1), ('u','v',3), ('s','v',1), ('v','t',2)]
    graph0 = GraphList()
    for v1, v2, e in graf_0:
        vertex1 = Vertex(v1)
        vertex2 = Vertex(v2)
        graph0.insert_vertex(vertex1)
        graph0.insert_vertex(vertex2)
        edge_t = Edge(e, True)
        edge_f = Edge(e, False)
        graph0.insert_edge(vertex1, vertex2, edge_f)
        graph0.insert_edge(vertex2, vertex1, edge_t)

    start = Vertex('s')
    end = Vertex('t')
    max_flow = 0

    while True:
        parent = BFS(graph0, start)
        minimum_capacity = min_capacity(graph0, start, end, parent)
        if minimum_capacity == 0:
            break
        path_augmentation(graph0, start, end, parent, minimum_capacity)
        max_flow += minimum_capacity

    print(max_flow)
    printGraph(graph0)

    graf_1 = [ ('s', 'a', 16), ('s', 'c', 13), ('c', 'a', 4), ('a', 'b', 12), ('b', 'c', 9), ('b', 't', 20), ('c', 'd', 14), ('d', 'b', 7), ('d', 't', 4) ]
    graph1 = GraphList()
    for v1, v2,  e in graf_1:
        vertex1 = Vertex(v1)
        vertex2 = Vertex(v2)
        graph1.insert_vertex(vertex1)
        graph1.insert_vertex(vertex2)
        edge_t = Edge(e, True)
        edge_f = Edge(e, False)
        graph1.insert_edge(vertex1, vertex2, edge_f)
        graph1.insert_edge(vertex2, vertex1, edge_t)

    start = Vertex('s')
    end = Vertex('t')
    max_flow = 0

    while True:
        parent = BFS(graph1, start)
        minimum_capacity = min_capacity(graph1, start, end, parent)
        if minimum_capacity == 0:
            break
        path_augmentation(graph1, start, end, parent, minimum_capacity)
        max_flow += minimum_capacity

    print(max_flow)
    printGraph(graph1)
        
    graf_2 = [ ('s', 'a', 3), ('s', 'c', 3), ('a', 'b', 4), ('b', 's', 3), ('b', 'c', 1), ('b', 'd', 2), ('c', 'e', 6), ('c', 'd', 2), ('d', 't', 1), ('e', 't', 9)]
    graph2 = GraphList()
    for v1, v2,  e in graf_2:
        vertex1 = Vertex(v1)
        vertex2 = Vertex(v2)
        graph2.insert_vertex(vertex1)
        graph2.insert_vertex(vertex2)
        edge_t = Edge(e, True)
        edge_f = Edge(e, False)
        graph2.insert_edge(vertex1, vertex2, edge_f)
        graph2.insert_edge(vertex2, vertex1, edge_t)

    start = Vertex('s')
    end = Vertex('t')
    max_flow = 0

    while True:
        parent = BFS(graph2, start)
        minimum_capacity = min_capacity(graph2, start, end, parent)
        if minimum_capacity == 0:
            break
        path_augmentation(graph2, start, end, parent, minimum_capacity)
        max_flow += minimum_capacity

    print(max_flow)
    printGraph(graph2)
    
if __name__ == "__main__":
    main()