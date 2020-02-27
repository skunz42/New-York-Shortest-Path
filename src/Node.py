class Node:
    def __init__(self, name, lat, lng, pop, priority):
        self.name = name
        self.lat = lat
        self.lng = lng
        self.pop = pop
        self.priority = priority
        self.adjList = []

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
