import re

class Bag:
    def __init__(self, name, children):
        self.name = name
        self.predecessors = []
        self.heldby = set()
        self.children = children

    def set_predecessor(self, pred):
        if pred not in self.predecessors:
            self.predecessors.append(pred)

    def num_parents(self):
        self.update_heldby()
        return len(self.heldby)

    def update_heldby(self):
        for bag in self.predecessors:
            self.heldby.add(bag)
            self.heldby.update(bag.update_heldby())
        return self.heldby

    def innercount(self):
        if not self.children:
            return 0
        count = 0
        for kid in self.children:
            count += kid[0]
            for bag in bags:
                if bag.name == kid[1]:
                    count += kid[0] * bag.innercount()
        return count

bags = []

f = open('input','r').readlines()

goldbag = Bag("noone cares", [])

for l in f:
    name = re.match(r"([a-z]+ [a-z]+) bags contain .*", l).group(1)
    contents = [(int(inner.group(1)), inner.group(2)) for inner in re.finditer(r"([0-9]) ([a-z]+ [a-z]+) bag", l)]
    newbag = Bag(name, contents)
    bags.append(newbag)
    if newbag.name == "shiny gold":
        goldbag = newbag

for bag in bags:
    for bag2 in bags:
        if bag.name == bag2.name:
            continue
        if bag.name in [kid[1] for kid in bag2.children]:
            bag.set_predecessor(bag2)

print(goldbag.num_parents())
print(goldbag.innercount())
