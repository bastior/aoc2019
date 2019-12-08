import ChallengeIf


class Day6Challenge1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = [a for a in open("input1.txt", 'r').read().split()]
        self.TestInputs = [[a for a in open("testin", 'r').read().split()]]
        self.TestOutputs = [42]

    def Run(self, arg):
        print(arg)
        iteration = 0
        sum = 0
        curr = ["COM"]
        while len(arg) > 0:
            new_curr = []
            sum += (iteration * len(curr))
            for c in curr:
                new_curr.extend([x for x in arg if x[:3] == c])
            print(new_curr)
            for nc in new_curr:
                arg.remove(nc)
            curr = [x[4:7] for x in new_curr]
            new_curr.clear()
            iteration += 1
        return sum + (iteration * len(curr))

obj = Day6Challenge1()
#obj.Test()
obj.Solve()
