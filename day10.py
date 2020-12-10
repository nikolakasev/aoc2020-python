# from https://www.geeksforgeeks.org/count-possible-paths-two-vertices/
class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def addEdge(self, u, v):

        # Add v to u’s list.
        self.adj[u].append(v)

    # Returns count of paths from 's' to 'd'
    def countPaths(self, s, d):

        # Mark all the vertices
        # as not visited
        visited = [False] * self.V

        # Call the recursive helper
        # function to print all paths
        pathCount = [0]
        self.countPathsUtil(s, d, visited, pathCount)
        return pathCount[0]

    # A recursive function to print all paths
    # from 'u' to 'd'. visited[] keeps track
    # of vertices in current path. path[]
    # stores actual vertices and path_index
    # is current index in path[]
    def countPathsUtil(self, u, d,
                       visited, pathCount):
        visited[u] = True

        # If current vertex is same as
        # destination, then increment count
        if (u == d):
            pathCount[0] += 1

        # If current vertex is not destination
        else:

            # Recur for all the vertices
            # adjacent to current vertex
            i = 0
            while i < len(self.adj[u]):
                if (not visited[self.adj[u][i]]):
                    self.countPathsUtil(self.adj[u][i], d,
                                        visited, pathCount)
                i += 1

        visited[u] = False


a = []
for line in open('day10.txt').read().split('\n'):
    a.append(int(line))


device = max(a) + 3
# add the own device and the charging outlet
a = sorted(a + [device] + [0])

one = 0
three = 0

# assume there will be no difference of two, so only a difference of one and three
for i in range(len(a)-1):
    if a[i+1] - a[i] == 1:
        one += 1
    else:
        three += 1

print(one*three)

print(len(a), list(enumerate(a)))

g = Graph(len(a))

for i in range(len(a)):
    if (i + 3) < len(a):
        if a[i + 3] - a[i] <= 3:
            print(f"add {i} -> {i + 3}")
            g.addEdge(i, i + 3)

    if (i + 2) < len(a):
        if a[i + 2] - a[i] <= 3:
            print(f"add {i} -> {i + 2}")
            g.addEdge(i, i + 2)

    if (i + 1) < len(a):
        if a[i + 1] - a[i] <= 3:
            print(f"add {i} -> {i + 1}")
            g.addEdge(i, i + 1)

print(g.countPaths(0, len(a) - 1))
