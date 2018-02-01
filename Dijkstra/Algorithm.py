import heapq

class Dijkstra(object):

    def __init__(self):
        self.numberOfIteration = 0
        self.verticlesToBeCalculated = []

    def findShortestPath(self, verticlesList, startingVertex):
        startingVertex.minimumDistance = 0
        heapq.heappush(self.verticlesToBeCalculated, startingVertex)

        while len(self.verticlesToBeCalculated) > 0:

            checkedVertex = heapq.heappop(self.verticlesToBeCalculated)

            for edge in checkedVertex.adjacentEdges:
                newDistance = checkedVertex.minimumDistance + edge.length
                if newDistance < edge.endVertex.minimumDistance:
                    edge.endVertex.predecessor = checkedVertex
                    heapq.heappush(edge.endVertex)
            self.printIteration()

    def printIteration(self):
        self. numberOfIteration += 1
        print('Dijkstra iteration: {}'.format(self.numberOfIteration))
        for vertex in self.verticlesToBeCalculated:
            print('Name:{}, value: {}'.format(vertex.name, vertex.minimumDistance))

