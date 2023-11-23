class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def is_safe(self, node, color, colored):
        for neighbor in self.graph[node]:
            if neighbor in colored and colored[neighbor] == color:
                return False
        return True

    def color_graph(self):
        colored = {}
        colors = ['Red', 'Blue', 'Green', 'Yellow', 'Orange', 'Purple']  

        for node in self.graph:
            for color in colors:
                if self.is_safe(node, color, colored):
                    colored[node] = color
                    break

        return colored


regions_graph = Graph()
regions_graph.add_edge('A', 'B')
regions_graph.add_edge('A', 'C')
regions_graph.add_edge('B', 'C')
regions_graph.add_edge('B', 'D')
regions_graph.add_edge('C', 'D')
regions_graph.add_edge('C', 'E')
regions_graph.add_edge('D', 'E')

colored_map = regions_graph.color_graph()
print("Colored Map:")
for node, color in colored_map.items():
    print(f"Region {node} is colored {color}")
