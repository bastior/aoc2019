import ChallengeIf


class Day1Challenge1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = [int(a) for a in open("input1.txt", 'r').read().split()]
        self.TestInputs = [[1969], [100756]]
        self.TestOutputs = [966, 50346]

    def Run(self, arg):
        sum = 0
        for input in arg:
            curr = input
            while True:
                curr = int(curr/3) - 2
                if curr <= 0:
                    break
                sum += curr
        return sum


obj = Day1Challenge1()
obj.Test()
#obj.Solve()
