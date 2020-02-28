import sys

class Node:
    def __init__(self, name, lat, lng, pop, priority):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.pop = pop
        self.priority = priority
        self.adjList = []

        self.dist = float("inf") # dist from source
        self.prev = None # predecessor
        self.visited = False

    # Override
    def __lt__(self, other):
        return self.dist < other.dist

    def getName(self):
        return self.name

    def getLat(self):
        return self.lat

    def getLng(self):
        return self.lng

    def getPop(self):
        return self.pop

    def getPriority(self):
        return self.priority

    def setAdjList(self, e):
        self.adjList.append(e)

    def getAdjList(self):
        return self.adjList

    def getDist(self):
        return self.dist

    def getPrev(self):
        return self.prev

    def setDist(self, dist):
        self.dist = dist

    def setPrev(self, prev):
        self.prev = prev

    def getVisited(self):
        return self.visited

    def setVisited(self, bool):
        self.visited = bool
