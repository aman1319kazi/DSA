class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph = {}

        for start, end in self.edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]
        print(self.graph)

    def getPaths(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return []

        allpaths = []
        for node in self.graph[start]:
            new_paths = self.getPaths(node, end, path)
            for p in new_paths:
                allpaths.append(p)
        return allpaths




if __name__ == '__main__':

    routes = [
        ("Mumbai","Pune"),
        ("Mumbai", "Surat"),
        ("Surat", "Bangaluru"),
        ("Pune","Hyderabad"),
        ("Pune","Mysuru"),
        ("Hyderabad","Bangaluru"),
        ("Hyderabad", "Chennai"),
        ("Mysuru", "Bangaluru"),
        ("Chennai", "Bangaluru")
    ]

    routes = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto"),
    ]

    route_graph = Graph(routes)
    print(route_graph.getPaths("New York", "Toronto"))

    start = "Mumbai"
    end = "New York"

    