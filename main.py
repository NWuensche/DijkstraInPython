#!/user/bin/env python3
# -*- coding: utf-8 -*-

from parser import *

def print_matrix(m):
    for i in m:
        for j in i:
            print('{0:3d}'.format(j),end='')
        print ('', end='\n')


def main():
    p = InputParser()
    adj = p.get_input()
    print("\nAdjacency matrix is:\n")
    print_matrix(adj)

if __name__ == '__main__':
    main()