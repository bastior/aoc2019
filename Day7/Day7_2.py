import ChallengeIf
import itertools


class Amp:
    def __init__(self, memory, thruster_setting):
        self.instruction_pointer = 0
        self.memory = memory[:]
        self.stop_cond = False
        self.thruster_setting_set = False
        self.thruster_setting = thruster_setting
        self.input = 0
        self.output_set = False
        self.output = 0

    def process(self):
        self.output_set = False
        opcode = self.memory[self.instruction_pointer]
        opcode = [int(x) for x in str(opcode)]
        while len(opcode) != 4:
            opcode.insert(0, 0)
        actual_opcode = opcode[3]
        mode1 = opcode[1]
        mode2 = opcode[0]
        if actual_opcode == 1 or actual_opcode == 2:
            f_o = self.memory[self.instruction_pointer + 1] if mode1 else self.memory[self.memory[self.instruction_pointer + 1]]
            s_o = self.memory[self.instruction_pointer + 2] if mode2 else self.memory[self.memory[self.instruction_pointer + 2]]
            self.memory[self.memory[self.instruction_pointer + 3]] = f_o * s_o if actual_opcode == 2 else f_o + s_o
            self.instruction_pointer += 4
        elif actual_opcode == 3 or actual_opcode == 4:
            if actual_opcode == 3:
                target = self.instruction_pointer + 1 if mode1 else self.memory[self.instruction_pointer + 1]
                if not self.thruster_setting_set:
                    self.memory[target] = self.thruster_setting
                    self.thruster_setting_set = True
                else:
                    self.memory[target] = self.input
            else:
                self.output = self.memory[self.instruction_pointer + 1] if mode1 else self.memory[self.memory[self.instruction_pointer + 1]]
                self.output_set = True
            self.instruction_pointer += 2
        elif actual_opcode == 5 or actual_opcode == 6:
            f_o = self.memory[self.instruction_pointer + 1] if mode1 else self.memory[self.memory[self.instruction_pointer + 1]]
            s_o = self.memory[self.instruction_pointer + 2] if mode2 else self.memory[self.memory[self.instruction_pointer + 2]]
            if (f_o != 0 and actual_opcode == 5) or (f_o == 0 and actual_opcode == 6):
                self.instruction_pointer = s_o
            else:
                self.instruction_pointer += 3
        elif actual_opcode == 7 or actual_opcode == 8:
            f_o = self.memory[self.instruction_pointer + 1] if mode1 else self.memory[self.memory[self.instruction_pointer + 1]]
            s_o = self.memory[self.instruction_pointer + 2] if mode2 else self.memory[self.memory[self.instruction_pointer + 2]]
            self.memory[self.memory[self.instruction_pointer + 3]] = 1 if (actual_opcode == 7 and f_o < s_o) or (actual_opcode == 8 and f_o == s_o) else 0
            self.instruction_pointer += 4
        else:
            self.stop_cond = True

class Day7Challenge2(ChallengeIf.ChallengeIf):
    def __init__(self):
        self.Input = [int(a) for a in open("input1.txt", 'r').read().split(",")]
        self.TestInputs = [[3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]]
        self.TestOutputs = [139629729]

    def Run(self, arg_in):
        thruster_setting_range = range(5,10)
        settings_set = itertools.permutations(thruster_setting_range, 5)
        max_val = 0
        for setting in settings_set:
            amplis = [Amp(arg_in, x) for x in setting]
            amp_index = 0
            output = 0
            while True:
                while True:
                    amp = amplis[amp_index % 5]
                    amp.input = output
                    amp.process()
                    if amp.output_set or amp.stop_cond:
                        amp_index += 1
                        output = amp.output
                        break
                if amplis[-1].stop_cond:
                    output=amplis[-1].output
                    if output > max_val:
                        max_val = output
                    break
        return max_val


obj = Day7Challenge2()
#obj.Test()
obj.Solve()
