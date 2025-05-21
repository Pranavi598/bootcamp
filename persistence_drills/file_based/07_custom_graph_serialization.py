import pickle


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, node1, node2):
        if node1 not in self.edges:
            self.edges[node1] = []
        self.edges[node1].append(node2)

    def to_pickle(self):
        # Custom serialization logic:
        # Serialize nodes and edges separately for more control
        return pickle.dumps({
            'nodes': list(self.nodes),
            'edges': self.edges
        })

    @classmethod
    def from_pickle(cls, pickle_data):
        data = pickle.loads(pickle_data)
        graph = cls()
        for node in data['nodes']:
            graph.add_node(node)
        for node1, neighbors in data['edges'].items():
            for node2 in neighbors:
                graph.add_edge(node1, node2)
        return graph

    def __repr__(self):
        return f"Graph(nodes={self.nodes}, edges={self.edges})"


def main():
    # Create a graph instance and add nodes/edges
    graph = Graph()
    graph.add_node("A")
    graph.add_node("B")
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")

    # Serialize the graph to a pickle file
    serialized_graph = graph.to_pickle()

    # Save the serialized graph to a file
    with open("graph.pkl", "wb") as f:
        f.write(serialized_graph)

    print("Graph serialized to graph.pkl")

    # Deserialize the graph from the file
    with open("graph.pkl", "rb") as f:
        serialized_data = f.read()

    deserialized_graph = Graph.from_pickle(serialized_data)
    print("Deserialized Graph object:", deserialized_graph)


if __name__ == "__main__":
    main()
