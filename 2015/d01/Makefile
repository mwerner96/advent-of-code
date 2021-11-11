CC = gcc -O3
SOLUTIONS = part1.out part2.out

solve: $(SOLUTIONS)
	./part1.out < input
	./part2.out < input

%.out: %.c
	$(CC) $< -o $@

.PHONY: solve
