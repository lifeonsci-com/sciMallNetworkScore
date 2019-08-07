from collections import defaultdict

class Graph(object):
    def __init__(self, dataframeGraph):
        self.graph = defaultdict(list)

        for index, row in dataframeGraph.iterrows():
            self.toGraph(row)

        print (self.graph)

    def toExcel(self):
        pass

    def toGraph(self, row):
        Source = row['Gene_1']
        Target = row['Gene_2']
        self.addEdge(Source, Target)

    def addEdge(self,u,v):
        self.graph[u].append(v)





