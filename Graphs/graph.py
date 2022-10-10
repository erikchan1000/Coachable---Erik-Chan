class Graph:
    def __init__(self, V):
        self._V = V
        self._E = 0

        self._adj = [[] for i in range(V)]

    def V(self):
        return self._V

    def E(self):
        return self._E

    def addEdge(self, vertices1, vertices2):
        self.validateVertex(vertices1)
        self.validateVertex(vertices2)

        self._E += 1
        self._adj[vertices1].append(vertices2)
        self._adj[vertices2].append(vertices1)

    def adj(self, vertex):
        self.validateVertex(vertex)
        return self._adj[vertex]

    def validateVertex(self, vertex):
        if vertex < 0 or vertex >= self._V:
            raise Exception(f"vertex: {str(vertex)} is not between 0 and {str(self._V - 1)}")

if __name__ == "__main__":
    # We can use this array to convert intgers stored in the graph back to 
    # the real-world names.
    vertices = ["Albert", "Bob", "Christa", "Danielle"]
    V = len(vertices)
    G = Graph(V)

    # Add the relationships 
    G.addEdge(0,1)
    G.addEdge(0,2)
    G.addEdge(0,3)
    G.addEdge(2,3)
    

    print(G.adj(0)) # 1,2,3 
    print(str(G))
    print(G._adj)