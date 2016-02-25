#!/user/bin/env python3
# -*- coding: utf-8 -*-

from parser import *
from calculate_shortest_way import *

def print_matrix(m):
    for i in m:
        for j in i:
            print('{0:3d}'.format(j),end='')
        print ('', end='\n')
    print('')


def main():
    p = InputParser()
    adj = p.get_input()
    print("\nAdjacency matrix is:\n")
    print_matrix(adj)
    DG = ComputeTools(adj)
    print_matrix(DG.matrix)
    DG.calculateWholeDG()
    print_matrix(DG.matrix)

if __name__ == '__main__':
    main()
