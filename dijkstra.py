# -*- coding: utf-8 -*-

class Dijkstra:
    def __init__(self, adj, nodes, start):
        self.adj = adj
        self.nodes = nodes
        self.start = nodes.index(start)
        self.dists = [float('inf') for x in range(len(adj))]
        self.dists[self.start] = 0
        # speichert Kanten, über die kürzester Weg geht
        self.way = []



    # Baut liste der Entfernungen von s ausgehend auf
    def dist_list(self):
        dists = self.dists
        nodecount = len(self.adj)
        b_nodes = [-1 for x in range(nodecount)] # boundary nodes/Randknotenmenge
        i = self.start


        for l in range(nodecount):
            for j in range(nodecount):
                v = self.adj[i][j]
                if v>0 and v+dists[i] < dists[j]:
                    dists[j] = v+dists[i]
                    b_nodes[j] = i # Knoten und Vorgänger jedes Randknoten speichern

            i = self.minweight_node(b_nodes)
            print("\n")

            print(b_nodes)
            print(dists)
            print(i)

            self.build_path([i,b_nodes[i]])
            b_nodes[i] = -1

            print(b_nodes)

    def build_path(self, b_node):
        self.way.append(b_node)


    # Liefert Randknoten mit minimalem Abstand zum Start
    def minweight_node(self, b_nodes):
        if max(b_nodes)==-1: return -1
        minweight = min([self.dists[i] for i,j in enumerate(b_nodes) if j>-1])
        node = self.dists.index(minweight)
        return node

    # Gibt Entfernung zu einem Knoten aus dists wieder
    def dist_to(self, v2):
        self.dist_list()
        return self.dists[self.nodes.index(v2)]

    # Gibt Pfad von Knoten zu einen Knoten aus dists wieder
    def path_to(self, v2):
        pass


    # Ausgabe der kürzesten Wege von Knoten s zu allen anderen Knoten
    def print_list(self):
        for n in range(len(self.nodes)):
            print("   \u279c {0}: {1}".format(self.nodes[n], self.dists[n]))
