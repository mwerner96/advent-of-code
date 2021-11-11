CC = gcc -O3
SOLUTIONS = part1 part2

solve: $(SOLUTIONS)

part1: part1.out
	./part1.out < input

part2: part2.out
	./part2.out < input

%.out: %.c
	$(CC) $< -o $@

.PHONY: solve $(SOLUTIONS)
