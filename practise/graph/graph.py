class Node(object):
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    """Assumes src and dest are nodes"""
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.source
    def getDestination(self):
        return self.destination
    def __str__(self):
        return self.src.getName() + '->' \
        + self.dest.getName()
class Diagraph(object):
    """edges is a dict mapping each node to a list of
        its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges(node) = []
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        else:
            self.edges[src].append(dest)
    def childrenOg(self, node):
        return self.edges[node]
    
    def hasNode(self, node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise ValueError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->'\
                        + dest.getName() + '\n'
        return result[:-1] #omit Final newline
