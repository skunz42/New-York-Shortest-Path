import csv
import heapq
import sys

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
        slat = slng = dlat = dlng = 0.0
        s = self.getCity(src)
        slat = s.getLat()
        slng = s.getLng()
        d = self.getCity(dest)
        dlat = d.getLat()
        dlng = d.getLng()

        if s and d:
            dist = ((s.getLat()-d.getLat())**2 + (s.getLng()-d.getLng())**2)**0.5
            e = Edge(s.getName(), d.getName(), dist)
            self.edges.append(e)
            e = Edge(d.getName(), s.getName(), dist)
            self.edges.append(e)

    '''
        Adds additional nodes that are not created in the initial call
    '''
    def addtlEdges(self):
        self.addEdge("Binghamton, NY", "Scranton, PA")
        self.addEdge("Scranton, PA", "East Stroudsburg, PA")
        self.addEdge("East Stroudsburg, PA", "Newark, NJ")
        self.addEdge("Lake Placid, NY", "Plattsburgh, NY")
        self.addEdge("Lake Placid, NY", "Glens Falls, NY")
        self.addEdge("Massena, NY", "Malone, NY")

    '''
        Finds city given name
    '''
    def getCity(self, name):
        for n in self.nodes:
            if n.getName() == name:
                return n
        return None

    '''
        Calculates shortest path
        @param - srcStr - start city
        @param - destStr - dest city
    '''
    def dijkstra(self, srcStr, destStr):
        src = self.getCity(srcStr)
        dest = self.getCity(destStr)
        pq = []
        for n in self.nodes:
            n.setDist(float("inf"))
            n.setPrev(None)
            n.setVisited(False)
            heapq.heappush(pq, n)

        src.setDist(0.0)

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
                alt = minNode.getDist() + n.getDist() + (1000/neighbor.getPop())
                if alt < neighbor.getDist():
                    neighbor.setDist(alt)
                    neighbor.setPrev(minNode)
            heapq.heapify(pq)

        it = dest
        if dest is not None and it is not None:
            path = []
            #print(src.getName() + '\t' + dest.getName())
            while it != src:
                path.append(it.getName())
                if it is not None:
                    it = it.getPrev()
            path.append(src.getName())
            print(path[::-1])

    def makeMap(self):
        cs = set()
        for n in self.nodes:
            for m in self.nodes:
                if int(n.getPriority()) < 2 and int(m.getPriority()) < 2 and \
                n.getName() != m.getName() and m.getName() not in cs:
                    self.dijkstra(n.getName(), m.getName())
            cs.add(n.getName())

def main():
    g = Graph()
    g.createNodes()
    g.createEdges()
    g.addtlEdges()
    g.createAdjLists()
    #g.dijkstra(sys.argv[1], sys.argv[2])
    g.makeMap()
main()
