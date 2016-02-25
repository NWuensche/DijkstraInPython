# -*- coding: utf-8 -*-

class ComputeTools:
    def __init__(self,matrix):
        self.make_diagonal_zero(matrix)
        self.matrix = matrix

    # Führt den i-ten Schritt aus, um DG(i) zu berechnen
    def calculateDG(self,step):

        # 1. Schritt geht durch [0]-Zeile und -Spalte
        step -=1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                # Wenn keiner der Wege unendlich(-1), dann schaue ob
                #   neuer kürzester Weg da
                if(self.matrix[i][step] != -1 and self.matrix[step][j] != -1):
                    self.matrix[i][j] = min(self.matrix[i][j],
                            self.matrix[step][j]+self.matrix[i][step])

    def make_diagonal_zero(self,matrix):
        for i in range(len(matrix)):
            matrix[i][i] = 0

    def calculateWholeDG(self):
        for step in range(len(self.matrix)):
            self.calculateDG(step)
