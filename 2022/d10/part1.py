class CPU:
    def __init__(self, assembly):
        self.rx = 1
        self.clock = 1
        self.assembly = assembly

    def noop(self):
        pass

    def add(self, a):
        self.rx += a

    def decode(self):
        for instruction in self.assembly:
            operands = instruction.split()
            if operands[0] == "noop":
                yield self.noop
            elif operands[0] == "addx":
                yield self.noop
                yield lambda: self.add(int(operands[1]))
            else:
                raise NotImplementedError

    def debug(self, inspection_times=[]):
        microcode = self.decode()
        for time in inspection_times:
            while True:
                if self.clock == time:
                    yield self.rx*time
                    break
                op = next(microcode, None)
                if op == None:
                    return
                else:
                    op()
                self.clock += 1


cpu = CPU(open("input").read().splitlines())

print(sum(cpu.debug(range(20, 221, 40))))
