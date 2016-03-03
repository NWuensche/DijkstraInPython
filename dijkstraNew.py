class DijkstraNew:
    def __init__(self,edges,start):
        self.edges = edges
        self.take_shorter_edges() # Bei doppelten Kanten kürzere nehmen
        self.start = start
        self.edges_in_dijkstra = [] # Kanten, über die Dijkstra geht
        self.visible_edges = [] # Sichtbare Kanten
        self.visible_nodes = [start] # Besuchte Knoten
