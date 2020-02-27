class Edge:
    def __init__(self, source, dest, dist):
        self.source = source
        self.dest = dest
        self.dist = dist

    def getSource(self):
        return self.source

    def getDest(self):
        return self.dest

    def getDist(self):
        return self.dist        
