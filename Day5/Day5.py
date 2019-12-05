import ChallengeIf


class Day5Challenge1(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = [int(a) for a in open("input1.txt", 'r').read().split(",")]
        self.TestInputs = [[3,9,8,9,10,9,4,9,99,-1,8], [3,3,1107,-1,8,3,4,3,99]]
        self.TestOutputs = [0, 1]

    def Run(self, arg):
        input = 5
        output = 0
        iter = 0
        while True:
            opcode = arg[iter]
            opcode = [int(x) for x in str(opcode)]
            while len(opcode) != 4:
                opcode.insert(0, 0)
            actual_opcode = opcode[3]
            mode1 = opcode[1]
            mode2 = opcode[0]

            if actual_opcode == 1 or actual_opcode == 2:
                f_o = arg[iter+1] if mode1 else arg[arg[iter+1]]
                s_o = arg[iter+2] if mode2 else arg[arg[iter+2]]
                arg[arg[iter+3]] = f_o * s_o if actual_opcode == 2 else f_o + s_o
                iter += 4
            elif actual_opcode == 3 or actual_opcode == 4:
                if actual_opcode == 3:
                    target = iter+1 if mode1 else arg[iter+1]
                    arg[target] = input
                else:
                    output = arg[iter+1] if mode1 else arg[arg[iter+1]]
                iter += 2
            elif actual_opcode == 5 or actual_opcode == 6:
                f_o = arg[iter+1] if mode1 else arg[arg[iter+1]]
                s_o = arg[iter+2] if mode2 else arg[arg[iter+2]]
                if (f_o != 0 and actual_opcode == 5) or (f_o == 0 and actual_opcode == 6):
                    iter = s_o
                else:
                    iter += 3
            elif actual_opcode == 7 or actual_opcode == 8:
                f_o = arg[iter+1] if mode1 else arg[arg[iter+1]]
                s_o = arg[iter+2] if mode2 else arg[arg[iter+2]]
                arg[arg[iter + 3]] = 1 if (actual_opcode == 7 and f_o < s_o) or (actual_opcode == 8 and f_o == s_o) else 0
                iter += 4
            else:
                break
        return output


obj = Day5Challenge1()
#obj.Test()
obj.Solve()
