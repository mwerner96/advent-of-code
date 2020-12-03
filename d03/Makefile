all: part1 part2

part1: part1.cc input.h
	@echo "CXX		$@"
	@g++ $@.cc -o $@.out
	@./$@.out

part2: part2.cc input.h
	@echo "CXX		$@"
	@g++ $@.cc -o $@.out
	@./$@.out

input.h: input
	@echo "GEN		$@"
	@echo "#include <stdint.h>" > $@
	@echo "constexpr uint32_t input[] = {" >> $@
	@tr .# 01 < input | sed -E 's/(.*)/    0b\1,/' >> $@
	@echo "};" >> $@

clean:
	@echo "CLEAN"
	@rm -f input.h part1.out part2.out

.PHONY: all clean
