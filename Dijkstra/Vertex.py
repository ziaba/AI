from math import inf


class Vertex(object):

    def __init__(self, vertexName):
        self.name = vertexName
        self.predecessor = None
        self.adjacentEdges = []
        self.minimumDistance = inf
        self.visited = False #zoptymalizowac

    def __cmp__(self, other):
        return self.cmp(self.minimumDistance, other.minimumDistance)

    def __lt__(self, other):
        return self.minimumDistance < other.minimumDistance

    def __str__(self):
        if self.predecessor == None:
            return "{} with minimum distance: {}".format(self.name, self.minimumDistance)
        else:
            return "{} -> {} with minimum distance: {}".format(self.predecessor.name, self.name, self.minimumDistance)
