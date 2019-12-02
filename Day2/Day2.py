import ChallengeIf


class Day2Challenge1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = [int(a) for a in open("input1.txt", 'r').read().split(",")]
        self.TestInputs = [[1969], [100756]]
        self.TestOutputs = [966, 50346]

    def Run(self, arg):
        arg[1] = 12
        arg[2] = 2
        iter = 0
        print(arg)
        while True:
            print(arg[iter+3], arg[iter+2], arg[iter+1])
            if arg[iter] == 1:
                arg[arg[iter+3]] = arg[arg[iter + 2]] + arg[arg[iter + 1]]
            elif arg[iter] == 2:
                arg[arg[iter+3]] = arg[arg[iter + 2]] * arg[arg[iter + 1]]
            else:
                break
            iter += 4
            print(arg)
            print("kek")
        print(arg)
        return arg[0]


obj = Day2Challenge1()
#obj.Test()
obj.Solve()
