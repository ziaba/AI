import heapq

class Dijkstra(object):

    def findShortestPath(self, startingVertex):
        candidates = []
        startingVertex.minimumDistance = 0
        heapq.heappush(candidates, startingVertex)

        while len(candidates) > 0:
            checkedVertex = heapq.heappop(candidates)
            for edge in checkedVertex.adjacentEdges:
                if self.__isCheckedVertexCanditate(checkedVertex, edge):

                    if self.isDirectionConsistent:
                        edge.endVertex.predecessor = checkedVertex
                        edge.endVertex.minimumDistance = self.__calculateNewDistance(checkedVertex, edge.length)
                        heapq.heappush(candidates, edge.endVertex)

                    else:
                        edge.startVertex.predecessor = checkedVertex
                        edge.startVertex.minimumDistance = self.__calculateNewDistance(checkedVertex, edge.length)
                        heapq.heappush(candidates, edge.startVertex)

    def __isCheckedVertexCanditate(self, checkedVertex, edge):
        return self.__calculateNewDistance(checkedVertex, edge.length) < self.__calculateOldDistance(checkedVertex, edge)

    def __calculateNewDistance(self, checkedVertex, edgeLength):
        return checkedVertex.minimumDistance + edgeLength

    def __calculateOldDistance(self, checkedVertex, edge):
        if checkedVertex == edge.endVertex:
            self.isDirectionConsistent = False
            return edge.startVertex.minimumDistance
        else:
            self.isDirectionConsistent = True
            return edge.endVertex.minimumDistance

    def getShortestPath(self, startVertex, finalVertex):
        shortestPath=[]
        shortestPath.append(finalVertex)

        predecesor = finalVertex.predecessor
        while (predecesor != None) and (predecesor != startVertex):
            shortestPath.append(predecesor)
            predecesor = predecesor.predecessor
        return shortestPath
