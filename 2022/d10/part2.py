class CPU:
    def __init__(self, assembly):
        self.rx = 1
        self.clock = 0
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

    def execute(self, times=[]):
        microcode = self.decode()
        for time in times:
            op = next(microcode, None)
            if op == None:
                return
            else:
                yield (time, self.rx)
                op()
            self.clock += 1


class CRT:
    def __init__(self, cpu, width=40, heigth=6):
        self.cpu = cpu
        self.width = width
        self.heigth = heigth
        self.framebuf = [["." for _ in range(self.width)] for _ in range(self.heigth)]

    def draw(self):
        for line in self.framebuf:
            print("".join(line))

    def render(self):
        self.framebuf = [["." for _ in range(self.width)] for _ in range(self.heigth)]

        for time, sprite in self.cpu.execute(range(self.width * self.heigth)):
            line = time // self.width
            column = time % self.width
            if sprite-1 <= column <= sprite+1:
                self.framebuf[line][column] = "#"


cpu = CPU(open("input").read().splitlines())
crt = CRT(cpu)

crt.render()
crt.draw()
