class Packet:
    def __init__(self, bits):
        in_len = len(bits)
        self.version = int(bits[:3], 2)
        bits = bits[3:]
        self.type = int(bits[:3], 2)
        bits = bits[3:]
        if self.type == 4:
            self.value = 0
            while True:
                first = bits[0]
                self.value *= 16
                self.value += int(bits[1:5], 2)
                bits = bits[5:]
                if first == '0':
                    break
        else:
            self.id = int(bits[0], 2)
            bits = bits[1:]
            self.children = []
            if self.id == 0:
                self.sub_len = int(bits[:15], 2)
                bits = bits[15:]
                while sum((c.consumed for c in self.children)) < self.sub_len:
                    self.children.append(Packet(bits))
                    consumed = self.children[-1].consumed
                    bits = bits[consumed:]
            else:
                self.sub_pks = int(bits[:11], 2)
                bits = bits[11:]
                while len(self.children) < self.sub_pks:
                    self.children.append(Packet(bits))
                    consumed = self.children[-1].consumed
                    bits = bits[consumed:]

        self.consumed = in_len - len(bits)

    def version_sum(self):
        vsum = self.version
        if self.type != 4:
            for c in self.children:
                vsum += c.version_sum()
        return vsum


with open('input') as f:
    input = bin(int('f' + f.readline().strip(), 16))[6:]

print(Packet(input).version_sum())
