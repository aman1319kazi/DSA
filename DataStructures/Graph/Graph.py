class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph = {}

        for start, end in self.edges:
            if start in self.graph:
                self.graph[start].append(end)
            else:
                self.graph[start] = [end]

    def getPaths(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return []

        allpaths = []
        for node in self.graph[start]:
            if node not in path:
                new_paths = self.getPaths(node, end, path)
                for p in new_paths:
                    allpaths.append(p)
        return allpaths

    def shortest_path(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return None

        shortest = None
        for node in self.graph[start]:
            if node not in path:
                sp = self.shortest_path(node, end, path)
                if shortest is None or sp < shortest:
                    shortest = sp
        return shortest



if __name__ == '__main__':


    routes = [
        ("Mumbai", "kolkata"),
        ("Mumbai", "karnataka"),
        ("kolkata", "karnataka"),
        ("kolkata", "chennai"),
        ("karnataka", "chennai"),
        ("chennai", "tamilnadu"),
    ]

    route_graph = Graph(routes)
    print(route_graph.shortest_path("Mumbai", "tamilnadu"))
