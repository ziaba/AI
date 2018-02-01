from math import inf


class Vertex(object):

    def __init__(self, vertexName, adjacentVertices):
        self.name = vertexName
        self.predecessor = None
        self.adjacentEdges = []
        self.minimumDistance = inf
        self.visited = False #zoptymalizowac

    def __cmp__(self, other):
        return self.cmp(self.minimumDistance, other.minimumDistance)

    def __lt__(self, other):
        return self.minimumDistance < other.minimumDistance
