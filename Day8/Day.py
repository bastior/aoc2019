import ChallengeIf
import itertools


class Day8Challenge1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = list(open("input1.txt", 'r').read())
        self.TestInputs = [[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]]
        self.TestOutputs = [43210]

    def Run(self, arg_in):
        arg_in = [int(x) for x in arg_in]
        size = 25 * 6
        number_of_layers = int(len(arg_in) / size)
        layers = [[0, 0, 0] for i in itertools.repeat(None, number_of_layers)]
        for i, pix in enumerate(arg_in):
            layer = int(i/size)
            layers[layer][pix] += 1
        min_zeros = min(layers, key=lambda x: x[0])
        return min_zeros[1] * min_zeros[2]

obj = Day8Challenge1()
#obj.Test()
obj.Solve()
