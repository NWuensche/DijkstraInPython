# -*- coding: utf-8 -*-

class ComputeTools:
    def __init__(self,matrix):
        self.make_diagonal_zero(matrix)
        self.matrix = matrix


    def make_diagonal_zero(self,matrix):
        for i in range(len(matrix)):
            matrix[i][i] = 0
