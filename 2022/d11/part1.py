

class Monkey:
    def __init__(self, string):
        lines = string.splitlines()

        self.items = [int(n) for n in lines[1].strip("Starting items: ").split(", ")]

        a, op, b = lines[2].strip("Operation: new = ").split()
        operations = {
            "*": lambda x, y: x*y,
            "+": lambda x, y: x+y
        }
        self.operation = lambda old: operations[op](old, old if b == "old" else int(b))

        test = int(lines[3].split()[-1])
        target_true = int(lines[4].split()[-1])
        target_false = int(lines[5].split()[-1])
        self.target = lambda new: target_true if new % test == 0 else target_false

        self.inspection_count = 0

    def throw_items(self):
        while len(self.items) > 0:
            self.inspection_count += 1
            item = self.items.pop(0)
            item = self.operation(item)
            item //= 3
            yield self.target(item), item


class Game:
    def __init__(self, input, iterations=20):
        self.monkeys = [Monkey(block) for block in input.read().split("\n\n")]
        self.iterations = iterations

    def play(self):
        for _ in range(self.iterations):
            for monkey in self.monkeys:
                for target, item in monkey.throw_items():
                    self.monkeys[target].items.append(item)


g = Game(open("input"), 20)
g.play()

business = list(sorted(monkey.inspection_count for monkey in g.monkeys))
print(business[-1] * business[-2])
