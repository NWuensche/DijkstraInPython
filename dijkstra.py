# -*- coding: utf-8 -*-

class Dijkstra:
    def __init__(self, adj, start):
        self.adj = adj
        self.s = start
        self.dists = [0 for x in range(len(adj))]

    def minweight(self, verts):
        return min([x for x in verts if x>0])

    def dist_list(self):
        pass


