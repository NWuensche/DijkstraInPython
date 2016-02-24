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
        print (verts)
        return edges

