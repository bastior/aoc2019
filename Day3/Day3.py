import itertools

import ChallengeIf


class Day3Challenge1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = open("input", 'r').read().split('\n')
        self.TestInputs = [["U7,R6,D4,L4", "R8,U5,L5,D3"], ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"], ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51","U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]]
        self.TestOutputs = [6, 159, 135]

    def return_visited_list(self, args):
        pos = 0,0
        visited = [pos]
        for i in args:
            direction = i[0]
            steps = int(i[1:])
            while steps != 0:
                pos_li = list(visited[-1])
                if direction == 'U':
                    pos_li[0] += 1
                elif direction == 'R':
                    pos_li[1] += 1
                elif direction == 'D':
                    pos_li[0] -= 1
                elif direction == 'L':
                    pos_li[1] -= 1
                visited.append(tuple(pos_li))
                steps -= 1
        return visited

    def Run(self, arg):
        vis_first = self.return_visited_list(arg[0].split(","))
        vis_second = self.return_visited_list(arg[1].split(","))
        crossings = list(set(vis_first).intersection(vis_second))

        crossings.remove((0, 0))
        return min([abs(x[0]) + abs(x[1]) for x in crossings])



obj = Day3Challenge1()
#obj.Test()
obj.Solve()
