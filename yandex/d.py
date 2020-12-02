# Python program to print topological sorting of a DAG
from collections import defaultdict

a = [int(x) for x in input().split(' ')]
n = a[0]
m = a[1]
k = a[2]

a = [int(x) for x in input().split(' ')]
b = [*a]

a = [int(x) for x in input().split(' ')]
s = [*a]

rebra = []
for i in range(m):
    a = [int(x) for x in input().split(' ')]
    rebra.append([*a])
for r in range(len(rebra)):
    rebra[r][0] += b[rebra[r][1] - 1] - b[rebra[r][2] - 1]

npeople = [0 for x in range(n)]

for i in s:
    npeople[i - 1] += 1


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.weights = {}

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph[u].append(v)
        self.weights[(u, v)] = w

        # A recursive function used by topologicalSort

    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

                # Push current vertex to stack which stores result
        stack.insert(0, v)

        # The function to do Topological Sort. It uses recursive

    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

                # Print contents of stack
        return stack


g = Graph(n)
for i in rebra:
    g.addEdge(i[1] - 1, i[2] - 1, i[0])

good_moves = defaultdict(list)


def dijsktra(graph, initial, end):
    graph.edges = graph.graph
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path


gg = g.topologicalSort()


def weight(g, path):
    res = 0
    for i in range(1, len(path)):
        res += g.weights[(path[i - 1], path[i])]
    return res

fkdoapsfkdosp = defaultdict(list)
while gg:
    c = gg.pop()
    for ggg in gg:
        p = dijsktra(g, ggg, c)
        if type(p) is not str:
            w = weight(g, p)
            fkdoapsfkdosp[ggg].append(w)

asdfdsafds = {}
for i in fkdoapsfkdosp.keys():
    asdfdsafds[i] = max(fkdoapsfkdosp[i])


res = 0
for i in range(len(b)):
    res += b[i] * npeople[i]
    if asdfdsafds.get(i) and asdfdsafds.get(i) < 0:
        res -= asdfdsafds[i]
print(res)

