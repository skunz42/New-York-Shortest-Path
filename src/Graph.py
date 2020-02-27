import csv

from Node import Node
from Edge import Edge

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def createNodes(self):
        with open('nodes.csv', newline='') as csv_file:
            rd = csv.reader(csv_file)
            for r in rd:
                n = Node(r[0], float(r[1]), float(r[2]), int(r[3]), r[4])
                self.nodes.append(n)

    def createEdges(self):
        for n in self.nodes:
            for m in self.nodes:
                dist = ((n.getLat()-m.getLat())**2 + (n.getLng()-m.getLng())**2)**0.5
                if (dist < 0.6):
                    e = Edge(n.getName(), m.getName(), dist)
                    self.edges.append(e)

    def createAdjLists(self):
        for n in self.nodes:
            for e in self.edges:
                if e.getSource() == n.getName() and e.getSource() != e.getDest():
                    n.setAdjList(e)

        for n in self.nodes:
            for e in n.getAdjList():
                print(e.getSource() + " to " + e.getDest())

    def addEdge(self, src, dest):
        slat = 0.0
        slng = 0.0
        dlat = 0.0
        dlng = 0.0
        s = None
        d = None
        for n in self.nodes:
            if n.getName() == src:
                slat = n.getLat()
                slng = n.getLng()
                s = n
            if n.getName() == dest:
                dlat = n.getLat()
                dlng = n.getLng()
                d = n

        if s and d:
            dist = ((s.getLat()-d.getLat())**2 + (s.getLng()-d.getLng())**2)**0.5
            e = Edge(s.getName(), d.getName(), dist)
            self.edges.append(e)
            e = Edge(d.getName(), s.getName(), dist)
            self.edges.append(e)

def main():
    g = Graph()
    g.createNodes()
    g.createEdges()
    g.addEdge("Binghamton, NY", "Scranton, PA")
    g.addEdge("Scranton, PA", "East Stroudsburg, PA")
    g.addEdge("East Stroudsburg, PA", "Newark, NJ")
    g.addEdge("Lake Placid, NY", "Plattsburgh, NY")
    g.addEdge("Lake Placid, NY", "Glens Falls, NY")
    g.addEdge("Massena, NY", "Malone, NY")
    g.createAdjLists()
main()
