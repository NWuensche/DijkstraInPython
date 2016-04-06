# -*- coding: utf-8 -*-

class Dijkstra:
    def __init__(self, adj, nodes, start):
        self.adj = adj
        self.nodes = nodes
        self.start = nodes.index(start)
        self.dists = [float('inf') for x in range(len(adj))]
        self.dists[self.start] = 0
        # speichert Kanten, über die kürzester Weg geht
        self.nodes_shortest_way = [[self.nodes[self.start],self.nodes[self.start]]]



    # Baut liste der Entfernungen von s ausgehend auf
    def dist_list(self):
        dists = self.dists
        nodecount = len(self.adj)
        b_nodes = set([]) # boundary nodes/Randknotenmenge
        i = self.start


        for l in range(nodecount):
            for j in range(nodecount):
                v = self.adj[i][j]
                if v>0 and v+dists[i] < dists[j]:
                    dists[j] = v+dists[i]
                    b_nodes.add(j)
            # Speichert neue kürzteste Kante in Array
            # TODO: Weg zu Endknoten speichern, kürzeste Kante nicht unbedingt Teil des Weges
            self.nodes_shortest_way.append([self.nodes[i],self.nodes[self.minweight_node(b_nodes)]])
            i = self.minweight_node(b_nodes)
            b_nodes.discard(i)

    # Liefert Randknoten mit minimalem Abstand zum Start
    def minweight_node(self, b_nodes):
        if len(b_nodes)==0: return -1
        minweight = min([self.dists[x] for x in b_nodes])
        node = self.dists.index(minweight)
        # b_nodes.discard(node)
        return node

    # Gibt Entfernung zu einem Knoten aus dists wieder
    def dist_to(self, v2):
        self.dist_list()
        return self.dists[self.nodes.index(v2)]
    # Gibt Pfad von Knoten zu einen Knoten aus dists wieder
    def path_to(self, v2):
        path = [v2]
        currentNode = v2
        while(currentNode != self.nodes[self.start]):
            currentNode = self.get_next_node_on_path(currentNode)
            path.append(currentNode)
        path.reverse() # Weg ist nun richtig rum
        return path

    def get_next_node_on_path(self,currentNode):
        for edge in self.nodes_shortest_way:
            if edge[1] == str(currentNode) and edge[0]!=edge[1]:
                return edge[0]


    # Ausgabe der kürzesten Wege von Knoten s zu allen anderen Knoten
    def print_list(self):
        for n in range(len(self.nodes)):
            print("   \u279c {0}: {1}".format(self.nodes[n], self.dists[n]))
