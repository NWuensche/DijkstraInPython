#!/user/bin/env python3
# -*- coding: utf-8 -*-

from parser import *
from calculate_shortest_way import *
from dijkstra import *

def print_matrix(m):
    for i in m:
        for j in i:
            print('{0:6.1f}'.format(j).replace('-1.0',u' \u221e  '),end='')
        print ('', end='\n')
    print('')


def main():
    p = InputParser()
    adj = p.get_matrix()
    nodes = p.verts
    v1, v2 = p.get_path()

    print("\nAdjacency matrix is:\n")
    print_matrix(adj)

    d = Dijkstra(adj,nodes,v1)
    print ("Shortest way {0}-{1} (Dijkstra):".format(v1,v2),end='')
    print (d.path_to(v2))

    # DG = ComputeTools(adj)
    # print_matrix(DG.matrix)
    # DG.calculateWholeDG()
    # print_matrix(DG.matrix)

if __name__ == '__main__':
    main()
