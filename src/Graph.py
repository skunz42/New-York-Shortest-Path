import csv
import heapq

from Node import Node
from Edge import Edge

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    '''
        Creates nodes from csv
    '''
    def createNodes(self):
        with open('nodes.csv', newline='') as csv_file:
            rd = csv.reader(csv_file)
            for r in rd:
                n = Node(r[0], float(r[1]), float(r[2]), int(r[3]), r[4])
                self.nodes.append(n)

    '''
        Creates edges based on distance (~30 miles)
    '''
    def createEdges(self):
        for n in self.nodes:
            for m in self.nodes:
                dist = ((n.getLat()-m.getLat())**2 + (n.getLng()-m.getLng())**2)**0.5
                if (dist < 0.6):
                    e = Edge(n.getName(), m.getName(), dist)
                    self.edges.append(e)

    '''
        Creates the adjacency lists for each node
    '''
    def createAdjLists(self):
        for n in self.nodes:
            for e in self.edges:
                if e.getSource() == n.getName() and e.getSource() != e.getDest():
                    n.setAdjList(e)

    '''
        For manual edge creation
        @param - src - Starting city name
        @param dest - Ending city name
    '''
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

    def dijkstra(self, srcStr, destStr):
        src = None
        dest = None
        for n in self.nodes:
            if n.getName() == srcStr:
                src = n
            if n.getName() == destStr:
                dest = n

        pq = []
        src.setDist(0.0)
        for n in self.nodes:
            heapq.heappush(pq, n)

        minNode = None

        while pq:
            minNode = heapq.heappop(pq)
            if minNode == dest:
                break

            for n in minNode.getAdjList():
                dname = n.getDest()
                neighbor = None
                for m in self.nodes:
                    if m.getName() == dname:
                        neighbor = m
                neighbor.setVisited(True)
                alt = minNode.getDist() + n.getDist()
                if alt < neighbor.getDist():
                    neighbor.setDist(alt)
                    neighbor.setPrev(minNode)

            heapq.heapify(pq)

        it = dest
        if dest is not None and it is not None:
            path = []
            while it != src:
                path.append(it.getName())
                if it is not None:
                    it = it.getPrev()

            path.append(src.getName())
            print(path[::-1])

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
    g.dijkstra("Binghamton, NY", "Erie, PA")
main()
