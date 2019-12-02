import itertools

import ChallengeIf


class Day2Challenge2(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = [int(a) for a in open("input1.txt", 'r').read().split(",")]
        self.TestInputs = [[1969], [100756]]
        self.TestOutputs = [966, 50346]

    def Run(self, arg):
        arg[1] = 12
        arg[2] = 2
        for noun, verb in itertools.product(list(range(99)), repeat=2):
            iter = 0
            mod_arg = arg[:]
            mod_arg[1] = noun
            mod_arg[2] = verb
            while True:
                if mod_arg[iter] == 1:
                    mod_arg[mod_arg[iter+3]] = mod_arg[mod_arg[iter + 2]] + mod_arg[mod_arg[iter + 1]]
                elif arg[iter] == 2:
                    mod_arg[mod_arg[iter+3]] = mod_arg[mod_arg[iter + 2]] * mod_arg[mod_arg[iter + 1]]
                else:
                    break
                iter += 4
            print(mod_arg[0])
            if mod_arg[0] == 19690720:
                print(mod_arg[0])
                return 100*noun + verb



obj = Day2Challenge2()
#obj.Test()
obj.Solve()
