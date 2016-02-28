# -*- coding: utf-8 -*-
from math import *

class Dijkstra:
    def __init__(self, adj, nodes, start):
        self.adj = adj
        self.nodes = nodes
        self.s = start
        self.dists = [inf for x in range(len(adj))]
        self.dists[0] = 0


    # Baut liste der Entfernungen von s ausgehend auf
    def dist_list(self):
        dists = self.dists
        nodecount = len(self.adj)
        b_nodes = set([]) # boundary nodes/Randknotenmenge
        i = 0

        for l in range(nodecount):
            for j in range(nodecount):
                v = self.adj[i][j]
                if v>0 and v+dists[i] < dists[j]:
                    dists[j] = v+dists[i]
                    b_nodes.add(j)
            i = self.minweight_node(b_nodes)

    # Liefert Randknoten mit minimalem Abstand zum Start
    def minweight_node(self, b_nodes):
        minweight = min([self.dists[x] for x in b_nodes])
        node = self.dists.index(minweight)
        b_nodes.discard(node)
        return node

    def path_to(self, v2):

    # Ausgabe der kürzesten Wege von Knoten s zu alle anderen Knoten
    def print_list(self):
        print("Distance from Node "+ str(adj[self.s]) + " to:" )
        for node in range(len(self.adj)):
            print("\t\tNode "+str(adj[node])+ ": " + str(self.dists[node]))
