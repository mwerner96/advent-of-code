#include "input.h"
#include <iostream>

constexpr int get_cnt() {
    int pos = 30, cnt = 0;
    for (int i = 0; i < sizeof(input)/sizeof(uint32_t); i++) {
        cnt += !!(input[i] & (1 << pos));
        pos -= 3;
        pos += pos < 0 ? 31 : 0;
    }
    return cnt;
}

int main() {
    std::cout << get_cnt() << std::endl;
}
