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


    # Hauptfunktion in Dijkstra, gibt kürzesten Weg zu v2 aus
    def get_shortest_way(self,v2):

        while True:
            self.delete_unnecessary_edges()
