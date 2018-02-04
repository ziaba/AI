import  unittest
from Dijkstra.Algorithm import *
from Dijkstra.Edge import *
from Dijkstra.Vertex import *

class TestDijkstraAlgorithm(unittest.TestCase):
    def setUp(self):
        self.vertex_A = Vertex("A")
        self.vertex_B = Vertex("B")
        self.vertex_C = Vertex("C")
        self.vertex_D = Vertex("D")
        self.vertex_E = Vertex("E")
        self.vertex_F = Vertex("F")
        self.vertex_G = Vertex("G")
        self.vertex_H = Vertex("H")

        edge_AB = Edge(self.vertex_A, self.vertex_B, 8)
        edge_AC = Edge(self.vertex_A, self.vertex_C, 2)
        edge_AD = Edge(self.vertex_A, self.vertex_D, 5)

        edge_BD = Edge(self.vertex_B, self.vertex_D, 2)
        edge_BF = Edge(self.vertex_B, self.vertex_F, 13)

        edge_CD = Edge(self.vertex_C, self.vertex_D, 2)
        edge_CE = Edge(self.vertex_C, self.vertex_E, 5)

        edge_DF = Edge(self.vertex_D, self.vertex_F, 6)
        edge_DG = Edge(self.vertex_D, self.vertex_G, 3)
        edge_DE = Edge(self.vertex_D, self.vertex_E, 1)

        edge_EG = Edge(self.vertex_E, self.vertex_G, 1)

        edge_FG = Edge(self.vertex_F, self.vertex_G, 2)
        edge_FH = Edge(self.vertex_F, self.vertex_H, 3)

        edge_GH = Edge(self.vertex_G, self.vertex_H, 6)

        self.vertex_A.adjacentEdges = {edge_AC, edge_AB, edge_AD}
        self.vertex_B.adjacentEdges = {edge_AB, edge_BF, edge_BD}
        self.vertex_C.adjacentEdges = {edge_AC, edge_CD, edge_CE}
        self.vertex_D.adjacentEdges = {edge_CD, edge_DE, edge_DF, edge_DG}
        self.vertex_E.adjacentEdges = {edge_EG, edge_CE, edge_DE}
        self.vertex_F.adjacentEdges = {edge_BF, edge_DF, edge_FG, edge_FH}
        self.vertex_G.adjacentEdges = {edge_DG, edge_EG, edge_FG, edge_GH}
        self.vertex_H.adjacentEdges = {edge_FH, edge_GH}

        self.sut = Dijkstra()

    def test_path(self):
        self.sut.findShortestPath(self.vertex_A)
        result = self.sut.getShortestPath(self.vertex_A, self.vertex_H)
        #TODO write assertion
        for vertex in result:
             print(vertex)