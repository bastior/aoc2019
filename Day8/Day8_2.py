import ChallengeIf
import itertools


class Day8Challenge2(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = list(open("input1.txt", 'r').read())

    def Run(self, arg_in):
        arg_in = [int(x) for x in arg_in]
        size = 25 * 6
        number_of_layers = int(len(arg_in) / size)
        final_msg = [9]*size

        for i, pix in enumerate(arg_in):
            pixel_nr = i%size
            if final_msg[pixel_nr] != 0 and final_msg[pixel_nr] != 1:
                final_msg[pixel_nr] = pix


        return "".join(str(x) for x in final_msg)


obj = Day8Challenge2()
#obj.Test()
obj.Solve()
