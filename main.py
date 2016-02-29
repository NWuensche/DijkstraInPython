#!/user/bin/env python3
# -*- coding: utf-8 -*-

from parser import *
from calculate_shortest_way import *
from dijkstra import *

# Matrix mit Unicode multiline braces printen
def print_matrix(m):
    for i in range(len(m)):
        print(' \u23a7' if i==0 else ' \u23aa' if i<len(m)-1 else ' \u23a9',end='')
        for j in range(len(m)):
            print('{0:6.1f}'.format(m[i][j]).replace('-1.0',u' \u221e  '),end='')
        print('  \u23ab' if i==0 else '  \u23aa' if i<len(m)-1 else '  \u23ad',end='\n')
    print('')


def main():
    p = InputParser()
    adj = p.get_matrix()
    nodes = p.verts
    v1, v2 = p.get_path()

    print("\nAdjacency matrix is:\n")
    print_matrix(adj)

    # TODO: Evtl Quele und Senke angeben, falls existent

    d = Dijkstra(adj,nodes,v1)
    print("Shortest way {0} \u279c {1} (Dijkstra): ".format(v1,v2),end='')
    print(d.path_to(v2))

    print("Other distances from {0}:".format(v1))
    d.print_list()

    print("\nFloyd-Warshall:\n")
    DG = ComputeTools(adj)
    print_matrix(DG.matrix)
    DG.calculateWholeDG()
    print_matrix(DG.matrix)

if __name__ == '__main__':
    main()
