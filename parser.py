# -*- coding: utf-8 -*-

class InputParser:
    def __init__(self):
        self.nodes = None

    def get_matrix(self):

        print("Please enter nodes and edge weights")
        print("(format: '[[start,weight,end],[...],...]'")
        inp = input().strip()

        # Input als Liste von Kanten ([a,x,b]) parsen
        edges = ''.join(inp.split(']')).split('[')
        edges = [x.split(',') for x in edges if x]

        #Schaut, ob Input fehlerfrei ist
        if self.check_edges(edges):
            edges[0] = edges[0][0:3]

            # Ziel- und Endknoten als set zusammenfassen,
            # dann in Liste sortieren
            nodes_out = {x[0] for x in edges}
            nodes_in  = {x[2] for x in edges}
            nodes_out.update(nodes_in)
            self.nodes = sorted(list(nodes_out))
            return self.adjmatrix(edges)
        else:
            return self.get_matrix()

    def adjmatrix(self, edges):
        nodes = self.nodes
        # nxn Nullmatrix initialisieren mit n=|nodes|
        size = len(nodes)
        matrix = [[ -1 for i in range(size)] for j in range(size)]
        # Ausgehende Kanten für jeden Knoten bestimmen,
        # zugehörige gewichte in adj-Matrix speichern
        for n in nodes:
            adj = [e for e in edges if e[0]==n]
            for a in adj:
                matrix[nodes.index(n)][nodes.index(a[2])] = \
                    float(a[1])

        return matrix

    def check_edges(self,edges):
         #Schaut, ob zu viele oder zu wenig Argumente und ob der Weg ein float/int ist
         for edge in edges:
            if len(edge) == 4 and edge[3] == "":
                continue
            elif len(edge)>3 and edge[3]!="":
                print("Invalid Syntax: Too many arguments!")
                return False
            elif len(edge)<3:
                print("Invalid Syntax: Too few arguments!")
                return False
            else:
                try: float(edge[1])
                except ValueError:
                        print("Invalid Syntax: Weight has to be a (float) number!")
                        return False
            return True

    def get_path(self):
        print("Please specify path to minimize")
        print("(format: 'node1 node2')")
        return self.check_path(input().split())

    def check_path(self, path):
        # Prüfen ob eingegebene Knoten in der Knotenmenge sind
        if len(path)==2 and path[0] in self.nodes \
                        and path[1] in self.nodes:
            return path
        else:
            print("Invalid path.")
            return self.get_path()

    def graph_info(self, adj):
        sources = []
        sinks = []
        iso = []
        for i in range(len(adj)):

            # Nur -1 in Spalte, aber nicht in Zeile -> Quelle
            if max([adj[j][i] for j in range(len(adj))]) == -1 and \
               max(adj[i]) > -1:
                sources.append(self.nodes[i])

            # Nur -1 in Zeile, aber nicht in Spalte -> Senke
            elif max(adj[i]) == -1 and \
                 max([adj[j][i] for j in range(len(adj))]) > -1:
                sinks.append(self.nodes[i])

            # Nur -1 in Zeile/Spalte -> isoliert
            elif max(adj[i]) == -1:
                iso.append(self.nodes[i])

        if not sources: sources = ''
        if not sinks:   sinks = ''
        if not iso:     iso = ''

        return "{srcs} source{s1}{src}, {snks} sink{s2}{snk} and {isos} isolated node{s3}{iso}".format(
                srcs = len(sources),
                src  = self.to_str(sources),
                snks = len(sinks),
                snk  = self.to_str(sinks),
                isos = len(iso),
                iso  = self.to_str(iso),
                s1 = 's' if len(sources)!=1 else '',
                s2 = 's' if len(sinks)!=1 else '',
                s3 = 's' if len(iso)!=1 else '').replace('0 ', 'no ')

    # Gibt zu liste einen string im Format (1, 2, 3) wieder
    def to_str(self,list_):
        if not list_: return ''
        return ' (' + ', '.join(list_) + ')'


