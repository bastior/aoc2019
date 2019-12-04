import ChallengeIf


class Day4Challenge1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = [307237, 769058]
        #self.TestInputs = [["U7,R6,D4,L4", "R8,U5,L5,D3"], ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"], ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]]
        #self.TestOutputs = [6, 159, 135]

    @staticmethod
    def check(i):
        li = [int(x) for x in str(i)]
        return all(i <= j for i, j in zip(li, li[1:])) and any(i == j for i, j in zip(li, li[1:]))

    def Run(self, arg):
        s = 0
        for i in range(arg[0], arg[1]):
            if self.check(i):
                s += 1

        return s



obj = Day4Challenge1()
#obj.Test()
obj.Solve()
