class DijkstraNew:
    def __init__(self,edges,start):
        self.edges = edges
        self.take_shorter_edges() # Bei doppelten Kanten kürzere nehmen
        self.start = start
        self.edges_in_dijkstra = [] # Kanten, über die Dijkstra geht
        self.visible_edges = [] # Sichtbare Kanten
        self.visible_nodes = [start] # Besuchte Knoten

    # Falls doppelte Kanten zwischen Knoten, dann nur kürzesten lassen
    def take_shorter_edges(self):
        delete_edges = self.index_of_longer_edges()
        if(delete_edges != [] and delete_edges != None):
            delete_edges.sort()
            delete_edges.reverse()
            self.delete_long_edges(delete_edges)

    # Indizes der langen Kanten bekommen
    def index_of_longer_edges(self):
        delete_edges = []
        for i in range(len(self.edges)):
            for j in range(len(self.edges)):
                if i != j and self.edges[i][0] == self.edges[j][0] and \
                 self.edges[i][2] == self.edges[j][2]:
                    if self.edges[i][1] > self.edges[j][1] \
                     and i not in delete_edges:
                        delete_edges.append(i)
                    elif self.edges[i][1] < self.edges[j][1] \
                     and j not in delete_edges:
                        delete_edges.append(j)
        return delete_edges

    # Lange Kanten löschen
    def delete_long_edges(self,delete_edges):
        for edge in delete_edges:
            self.edges.pop(edge)

    # Alle Kanten markieren, die sichtbar sind und noch nicht besucht wurden
    def get_visible_edges(self):
        self.visible_edges = []
        for edge in self.edges:
            if edge[0] in self.visible_nodes:
                self.visible_edges.append(edge)

    # Wenn ich neuen Knoten besucht habe, dann alle ebageenden Kantne verlängern
    def make_edges_longer(self):
        for edge in range(len(self.edges)):
            if(self.edges[edge][0] == self.visible_nodes[-1]):
                self.edges[edge][1] += self.visible_edges[-1]

    # kürzeste, sichtbare Kante auswählen
    def get_shortest_edge(self):
        try:
            shortest_edge = self.visible_edges[0]# TODO try-catch, wenn Fehler, dann fertig
        except:
            return []
        for edge in self.visible_edges:
            if(shortest_edge[1] > edge[1]):
                shortest_edge = edge
        # Neuer Knoten erreichbar
        self.visible_nodes.append(shortest_edge[2])
        return shortest_edge

    #Löscht alle anderen Kanten, die zu schon besuchten Knoten gehen
    def delete_unnecessary_edges(self):
        delete_edges = []
        for edge in range(len(self.edges)):
            if(self.edges[edge][2] == self.visible_nodes[-1]):
                delete_edges.append(edge)
        if(delete_edges != [] and delete_edges != None):
            delete_edges.reverse()
            self.delete_long_edges(delete_edges)


    # Hauptfunktion in Dijkstra, gibt kürzesten Weg zu v2 aus
    def get_shortest_way(self,v2):

        while True:
            self.delete_unnecessary_edges()
            self.get_visible_edges()
            shortest_edge = self.get_shortest_edge()
            if(shortest_edge != []):
                self.edges_in_dijkstra.append(shortest_edge)
                self.visible_nodes.append(shortest_edge[2])
            else:
                break

        return self.shortest_way(v2)

    # Kürzesten Weg zu Knoten berechnen, unendlich, wenn kein Weg da
    def shortest_way(self,v2):
        way = [v2]
        currentNode = v2
        currentNodetmp = v2 # Wichtig, um zu schauen, ob Weg existiert
        while currentNode is not self.start:
            for edge in self.edges_in_dijkstra:
                if edge[2] == currentNode:
                    way.append(edge[0])
                    currentNodetmp = edge[0]
                    break
            if(currentNode == currentNodetmp): # Wenn Wahr, dann kein Weg da
                return float('inf')
            currentNode = currentNodetmp
        way.reverse()
        return way
