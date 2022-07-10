with open("input") as f:
    memory = [int(num) for num in f.readline().strip().split(",")]

memory[1] = 12
memory[2] = 2

for i in range(0, len(memory), 4):
    op = memory[i]
    if op == 1:
        memory[memory[i + 3]] = memory[memory[i + 1]] + memory[memory[i + 2]]
    elif op == 2:
        memory[memory[i + 3]] = memory[memory[i + 1]] * memory[memory[i + 2]]
        pass
    elif op == 99:
        print(memory[0])
        exit()
    else:
        raise
