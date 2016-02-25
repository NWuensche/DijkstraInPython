# -*- coding: utf-8 -*-

class InputParser:
    def __init__(self):
        pass

    def get_input(self):

        print("Please enter vertices and edge weights")
        print("(format: [[start,weight,end],[...],...]")
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
            verts = sorted(list(verts_out))
            return self.adjmatrix(verts,edges)
        else:
            return self.get_input()

    def adjmatrix(self, verts, edges):

        # nxn Nullmatrix initialisieren mit n=|verts|
        size = len(verts)
        matrix = [[ -1 for i in range(size)] for j in range(size)]
        # Ausgehende Kanten für jeden Knoten bestimmen,
        # zugehörige gewichte in adj-Matrix speichern
        for v in verts:
            adj = [e for e in edges if e[0]==v]
            for a in adj:
                matrix[verts.index(v)][verts.index(a[2])] = \
                    int(a[1])

        return matrix

    def check_edges(self,edges):
         #Schaut, ob zu viele oder zu wenig Argumente und ob alles Zahlen sind
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
                for item in edge:
                    if(not item.isdigit()):
                        print("Invalid Syntax: Just digits allowed!")
                        return False
            return True
