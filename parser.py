# -*- coding: utf-8 -*-

class InputParser:
    def __init__(self):
        self.verts = None

    def get_matrix(self):

        print("Please enter vertices and edge weights")
        print("(format: '[[start,weight,end],[...],...]'")
        inp = input()

        # Input als Liste von Kanten ([a,x,b]) parsen
        edges = ''.join(inp.split(']')).split('[')
        edges = [x.split(',') for x in edges if x]

        #Schaut, ob Input fehlerfrei ist
        if self.check_edges(edges):
            edges[0] = edges[0][0:3]

            # Ziel- und Endknoten als set zusammenfassen,
            # dann in Liste sortieren
            verts_out = {x[0] for x in edges}
            verts_in  = {x[2] for x in edges}
            verts_out.update(verts_in)
            self.verts = sorted(list(verts_out))
            return self.adjmatrix(edges)
        else:
            return self.get_matrix()

    def adjmatrix(self, edges):
        verts = self.verts
        # nxn Nullmatrix initialisieren mit n=|verts|
        size = len(verts)
        matrix = [[ -1 for i in range(size)] for j in range(size)]
        # Ausgehende Kanten für jeden Knoten bestimmen,
        # zugehörige gewichte in adj-Matrix speichern
        for v in verts:
            adj = [e for e in edges if e[0]==v]
            for a in adj:
                matrix[verts.index(v)][verts.index(a[2])] = \
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
        print("(format: 'vertex1 vertex2'")
        return self.check_path(input().split())

    def check_path(self, path):
        if len(path)==2 and path[0] in self.verts \
                        and path[1] in self.verts:

            return path
        else:
            print("Unknown vertices found.")
            return self.get_path()