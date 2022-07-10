with open("input") as f:
    input = [int(num) for num in f.readline().strip().split(",")]


for noun, verb in ((n, v) for n in range(100) for v in range(100)):
    memory = input.copy()
    memory[1] = noun
    memory[2] = verb

    for i in range(0, len(memory), 4):
        op = memory[i]
        if op == 1:
            memory[memory[i + 3]] = memory[memory[i + 1]] + memory[memory[i + 2]]
        elif op == 2:
            memory[memory[i + 3]] = memory[memory[i + 1]] * memory[memory[i + 2]]
            pass
        elif op == 99:
            break
        else:
            raise

    if memory[0] == 19690720:
        print(100 * noun + verb)
        exit()
