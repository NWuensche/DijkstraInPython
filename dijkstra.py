# -*- coding: utf-8 -*-

class Dijkstra:
    def __init__(self, adj, start):
        self.adj = adj
        self.s = start
        self.dists = [0 for x in range(len(adj))]

    # Liefert minimales Element > 0
    def minweight(self, verts):
        return min([x for x in verts if x>0])

    # Baut liste der Entfernungen von s ausgehend auf
    def dist_list(self):

        i = s

        for v in adj[i]:
            if v>0:
                self.dists[adj[s].index(v)] = v



