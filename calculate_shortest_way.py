# -*- coding: utf-8 -*-

class ComputeTools:
    def __init__(self,adj,nodes,start):
        self.make_diagonal_zero(adj)
        self.adj = adj
        self.start = nodes.index(start)
        self.nodes = nodes


    # Führt den i-ten Schritt aus, um DG(i) zu berechnen
    def calculateDG(self,step):

        # 1. Schritt geht durch [0]-Zeile und -Spalte
        step -=1
        for i in range(len(self.adj)):
            for j in range(len(self.adj)):
                # Wenn keiner der Wege unendlich(-1), dann schaue ob
                #   neuer kürzester Weg da
                if(self.adj[i][step] != -1 and self.adj[step][j] != -1):
                    self.adj[i][j] = min(self.adj[i][j],
                            self.adj[step][j]+self.adj[i][step])

    def make_diagonal_zero(self,adj):
        for i in range(len(adj)):
            adj[i][i] = 0

    def calculateWholeDG(self):
        for step in range(len(self.adj)):
            self.calculateDG(step)

    def print_list_floyd(self):
        self.calculateWholeDG()
        for n in range(len(self.nodes)):
            # TODO finde Buchstaben in Matrix
            print("   \u279c {0}: {1}".format(self.nodes[n], (self.adj[self.start][n])).replace("-1",u'inf' ))
