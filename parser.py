class InputParser:
    def __init__(self):
        pass

    def get_input(self):
        print("Please enter vertices and edge weights")
        print("(format: [[start,weight,end],[...],...]")
        inp = input()

        edges = ''.join(inp.split(']')).split('[')
        edges = [x.split(',') for x in edges if x]
        edges[0] = edges[0][0:3]

        verts = sorted(list({x[0] for x in edges}))
        return self.adjmatrix(verts,edges)

    def adjmatrix(self, verts, edges):
        size = len(verts)
        matrix = [[ 0 for i in range(size)] for j in range(size)]

        for v in verts:
            adj = [e for e in edges if e[0]==v]
            for a in adj:
                matrix[verts.index(v)][verts.index(a[2])] = \
                    int(a[1])

        return matrix
