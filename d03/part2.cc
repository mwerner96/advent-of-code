#include "input.h"
#include <iostream>

constexpr uint64_t get_cnt(int right = 3, int down = 1) {
    int pos = 30;
    uint64_t cnt = 0;
    for (int i = 0; i < sizeof(input)/sizeof(uint32_t); i += down) {
        cnt += !!(input[i] & (1 << pos));
        pos -= right;
        pos += pos < 0 ? 31 : 0;
    }
    return cnt;
}

int main() {
    constexpr uint64_t trees = get_cnt(1) * get_cnt() * get_cnt(5) * get_cnt(7) * get_cnt(1, 2);
    std::cout << trees << std::endl;
}
